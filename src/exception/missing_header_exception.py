class MissingHeaderException(Exception):
    """Raised when the expected header is not found"""
    def __init__(self, field: str) -> None:
        super().__init__(f"The following header is missing: {field}.")

    def get_code(self) -> int:
        return 7
