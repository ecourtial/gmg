class ResourceNotFoundException(Exception):
    """Raised when the expected resource is not found"""
    def __init__(self, type: str, id: int | str, key: str = 'id') -> None:
        if key == 'id':
            id = '#' + str(id)
        else:
            id = "'" + str(id) + "'"

        super().__init__(f"The resource of type '{type}' with {key} {id} has not been found.")

    def get_code(self) -> int:
        return 1
