from src.exception.inconsistent_operation import InconsistentOperation

class InconsistentTransactionTypeOperation(InconsistentOperation):
    """Raised when you try, for instance, to sold a copy you don't have"""
    def __init__(self, transaction_type, current_copy_status):
        msg = 'Inconsistent transaction. You tried to create a transaction of '
        msg += f"type '{transaction_type}' while the copy status is '{current_copy_status}'."
        super().__init__(msg)

    def get_code(self):
        return 4
