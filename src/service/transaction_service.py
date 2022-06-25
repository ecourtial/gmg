from src.exception.duplicate_consecutive_operation import DuplicateConsecutiveOperation
from src.exception.inconsistent_transaction_type_operation import InconsistentTransactionTypeOperation
from src.exception.inconsistent_version_and_copy_id import InconsistentVersionAndCopyIdException
from src.service.abstract_service import AbstractService
from src.repository.transaction_repository import TransactionRepository
from src.repository.copy_repository import CopyRepository
from src.repository.version_repository import VersionRepository
from src.entity.transaction import Transaction
from src.exception.unknown_resource_exception import ResourceNotFoundException

class TransactionService(AbstractService):
    resource_type = 'transaction'

    def __init__(self, mysql):
        self.repository = TransactionRepository(mysql)
        self.copy_repository = CopyRepository(mysql)
        self.version_repository = VersionRepository(mysql)

    def get_for_create(self):
        return super().validate_payload_for_creation_and_hydrate(Transaction)

    def get_for_update(self, transaction_id):
        transaction = self.repository.get_by_id(transaction_id)

        if transaction is None:
            raise ResourceNotFoundException('transaction', transaction_id)

        super().hydrate_for_update(transaction)

        return transaction

    def insert(self, object):
        version = self.get_version(object)
        copy = self.get_copy(object)
        self.check_no_duplicate_type_consecutive(copy, object)
        self.check_version_copy_consistency(version, copy)
        self.update_copy_status(object, copy)
        self.update_copy_id(object)

        commit = False
        if copy is None:
            commit = True

        object = self.repository.insert(object, commit)
        self.update_copy_in_db(object, copy)

        return object

    def update(self, object):
        version = self.get_version(object)
        copy = self.get_copy(object)
        self.check_no_duplicate_type_consecutive(copy, object)
        self.check_version_copy_consistency(version, copy)
        self.update_copy_status(object, copy)
        self.update_copy_id(object)

        commit = False
        if copy is None:
            commit = True

        object = self.repository.update(object, commit)
        self.update_copy_in_db(object, copy)

        return object

    def delete(self, transaction_id):
        transaction = self.repository.get_by_id(transaction_id)

        if transaction is None:
            raise ResourceNotFoundException('transaction', transaction_id)

        self.repository.delete(transaction_id)

        return True

    def get_version(self, transaction):
        version = self.version_repository.get_by_id(transaction.get_version_id())

        if version is None:
            raise ResourceNotFoundException('version', transaction.get_version_id())

        return version

    def get_copy(self, transaction):
        if transaction.get_copy_id() is not None:
            copy = self.copy_repository.get_by_id(transaction.get_copy_id())

            if copy is None:
                raise ResourceNotFoundException('copy', transaction.get_copy_id())

            return copy

        return None

    def check_version_copy_consistency(self, version, copy): #pylint: disable=no-self-use
        if (copy is not None and version.get_id() != copy.get_version_id()):
            raise InconsistentVersionAndCopyIdException(version.get_id(), copy.get_version_id())

    def update_copy_status(self, transaction, copy): #pylint: disable=no-self-use
        if copy is not None:
            # You cannot create an outbound transaction if you already don't have the copy anymore
            if transaction.get_type() in transaction.transaction_out and copy.get_status() == 'Out':
                raise InconsistentTransactionTypeOperation(transaction.get_type(), copy.get_status())

            if transaction.get_type() in transaction.transaction_in:
                copy.set_status('In')
            else:
                copy.set_status('Out')

    def update_copy_in_db(self, transaction, copy): #pylint: disable=no-self-use
        if copy is not None:
            if self.is_sold_transaction(transaction):
                self.repository.reset_copy_id_for_transactions(copy.get_id(), False)
                self.copy_repository.delete(copy.get_id())
            else:
                self.copy_repository.update(copy)

    def is_sold_transaction(self, transaction): #pylint: disable=no-self-use
        if transaction.get_type() == 'Sold':
            return True

        return False

    def update_copy_id(self, transaction):
        if self.is_sold_transaction(transaction):
            transaction.set_copy_id(None)

    def check_no_duplicate_type_consecutive(self, copy, transaction):
        if copy is not None:
            # You cannot create the same transaction type (Inbound or Outbound type) twice
            last_transaction_for_copy = self.repository.get_last_transaction_for_copy(copy.get_id())
            if last_transaction_for_copy is not None:
                if transaction.get_type() in transaction.transaction_out:
                    transaction_type = "outbound"
                else:
                    transaction_type = "inbound"

                if last_transaction_for_copy.get_type() in transaction.transaction_out:
                    last_transaction_type = "outbound"
                else:
                    last_transaction_type = "inbound"

                if transaction_type == last_transaction_type:
                    raise DuplicateConsecutiveOperation(transaction_type)
