from src.exception.inconsistent_operation import InconsistentOperation

class InconsistentVersionAndCopyIdException(InconsistentOperation):
    """Raised when you try to create a transaction for which version_id and the copy version_id don't match."""
    def __init__(self, transaction_version_id, copy_version_id):
        msg = 'Inconsistent transaction. You tried to create a transaction with versionId '
        msg += f"= '{transaction_version_id}' while the copy versionId is '{copy_version_id}'."
        super().__init__(msg)

    def get_code(self):
        return 14
