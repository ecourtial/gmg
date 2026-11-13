class MissingFieldException(Exception):
    """Raised when the expected field is not found"""
    def __init__(self, field: str) -> None:
        super().__init__(f"The following field is missing: {field}.")

    def get_code(self) -> int:
        return 6
