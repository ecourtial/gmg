class ResourceNotFoundException(Exception):
    """Raised when the expected resource is not found"""
    def __init__(self, type, id):
        super().__init__(f"The resource of type '{type}' with id  #{id} has not been found.")
