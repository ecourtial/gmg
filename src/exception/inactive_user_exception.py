class InactiveUserException(Exception):
    def __init__(self, field, value):
        super().__init__(f"The user with {field} = {value} is inactive.")

    def get_code(self):
        return 3
