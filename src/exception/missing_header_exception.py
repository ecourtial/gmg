class MissingHeaderException(Exception):
    """Raised when the expected header is not found"""
    def __init__(self, field):
        super().__init__(f"The following header is missing: {field}.")

    def get_code(self):
        return 7
