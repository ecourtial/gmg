class UnsupportedValueException(Exception):
    def __init__(self, field: str, value: str, supported_values: set[str]) -> None:
        super().__init__(f"The field '{field}' does not support the value '{value}'. Supported values are: " + ', '.join(sorted(supported_values)) + '.')

    def get_code(self) -> int:
        return 11
