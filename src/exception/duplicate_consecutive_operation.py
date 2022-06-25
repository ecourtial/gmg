from src.exception.inconsistent_operation import InconsistentOperation

class DuplicateConsecutiveOperation(InconsistentOperation):
    """Raised when you try, for instance, to create two consecutive inbound transaction"""
    def __init__(self, transaction_type):
        msg = 'Inconsistent transaction. You tried to create a transaction an '
        msg += f"{transaction_type} transaction while the last registered "
        msg += 'transaction for this copy has of the same kind!'
        super().__init__(msg)

    def get_code(self):
        return 15
