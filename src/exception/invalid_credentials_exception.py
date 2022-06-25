class InvalidCredentialsException(Exception):
    def __init__(self):
        super().__init__(f"The credentials are invalid.")

    def get_code(self):
        return 2
