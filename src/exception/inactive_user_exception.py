class InactiveUserException(Exception):
    def __init__(self, field: str, value: str) -> None:
        super().__init__(f"The user with {field} = {value} is inactive.")

    def get_code(self) -> int:
        return 3
