class InvalidCredentialsException(Exception):
    def __init__(self) -> None:
        super().__init__("The credentials are invalid.")

    def get_code(self) -> int:
        return 2
