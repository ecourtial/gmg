class ResourceAlreadyExistsException(Exception):
    """Raised when the expected resource already exists"""
    def __init__(self, type, id, key = 'id'):
        if key == 'id':
            id = '#' + id
        else :
            id = "'" + id + "'"

        super().__init__(f"The resource of type '{type}' with {key} {id} already exists.")

    def get_code(self):
        return 8
