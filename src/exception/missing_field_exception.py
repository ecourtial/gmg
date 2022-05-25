class MissingFieldException(Exception):
    """Raised when the expected field is not found"""
    def __init__(self, field):
        super().__init__(f"The following field is missing: {field}.")
