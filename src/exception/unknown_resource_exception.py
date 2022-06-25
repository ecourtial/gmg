class ResourceNotFoundException(Exception):
    """Raised when the expected resource is not found"""
    def __init__(self, type, id, key = 'id'):
        if key == 'id':
            id = '#' + str(id)
        else :
            id = "'" + id + "'"

        super().__init__(f"The resource of type '{type}' with {key} {id} has not been found.")

    def get_code(self):
        return 1
