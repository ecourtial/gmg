class InvalidInput(Exception):
    """Raised when the expected value is not good, inconsistent..."""

    def get_code(self) -> int:
        return 5
