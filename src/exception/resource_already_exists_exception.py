class ResourceAlreadyExistsException(Exception):
    """Raised when the expected resource already exists"""
    def __init__(self, type: str, id: str, key: str = 'id') -> None:
        if key == 'id':
            id = '#' + id
        else:
            id = "'" + id + "'"

        super().__init__(f"The resource of type '{type}' with {key} {id} already exists.")

    def get_code(self) -> int:
        return 8
