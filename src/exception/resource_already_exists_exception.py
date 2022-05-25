class ResourceAlreadyExistsException(Exception):
    """Raised when the expected resource already exists"""
    def __init__(self, type, id):
        super().__init__(f"The resource of type '{type}' with id  #{id} already exists.")