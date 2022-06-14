class InvalidInput(Exception):
    """Raised when the expected value is not good, inconsistent..."""

    def get_code(self):
        return 5
