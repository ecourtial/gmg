class UnsupportedValueException(Exception):
    def __init__(self, field, value, supported_values):
        super().__init__(f"The field '{field}' does not support the value '{value}'. Supported values are: " + ', '.join(sorted(supported_values)) + '.')
