from src.exception.inconsistent_operation import InconsistentOperation
from src.service.abstract_service import AbstractService
from src.repository.transaction_repository import TransactionRepository
from src.repository.copy_repository import CopyRepository
from src.entity.transaction import Transaction
from src.exception.unknown_resource_exception import ResourceNotFoundException

class TransactionService(AbstractService):
    resource_type = 'transaction'

    def __init__(self, mysql):
        self.repository = TransactionRepository(mysql)
        self.copy_repository = CopyRepository(mysql)

    def get_for_create(self):

        transaction = super().validate_payload_for_creation_and_hydrate(Transaction)
        copy = self.copy_repository.get_by_id(transaction.get_copy_id())

        if copy is None:
            raise ResourceNotFoundException('copy', transaction.get_copy_id())

        self.validate_transaction_status(copy, transaction)
        self.copy_repository.update(copy, False) # False is important here

        return transaction

    def get_for_update(self, transaction_id):
        transaction = self.repository.get_by_id(transaction_id)

        if transaction is None:
            raise ResourceNotFoundException('transaction', transaction_id)

        super().hydrate_for_update(transaction)

        copy = self.copy_repository.get_by_id(transaction.get_copy_id())

        if copy is None:
            raise ResourceNotFoundException('copy', transaction.get_copy_id())

        self.validate_transaction_status(copy, transaction)
        self.copy_repository.update(copy, False) # False is important here

        return transaction

    def delete(self, transaction_id):
        transaction = self.repository.get_by_id(transaction_id)

        if transaction is None:
            raise ResourceNotFoundException('transaction', transaction_id)

        self.repository.delete(transaction_id)

        return True

    def validate_transaction_status(self, copy, transaction):#pylint: disable=no-self-use
        """Check if the transaction is legit and toggle the status of the copy"""
        if ((transaction.get_type() in transaction.transaction_in and copy.get_status() == 'In') or
            (transaction.get_type() in transaction.transaction_out and copy.get_status() == 'Out')):
            raise InconsistentOperation(transaction.get_type(), copy.get_status())

        if transaction.get_type() in transaction.transaction_in:
            copy.set_status('In')
        else:
            copy.set_status('Out')
