class UnsupportedFilterException(Exception):
    def __init__(self, field, allowed_filters):
        super().__init__(f"The following filter is not allowed: {field}. Allowed filters are: " + ', '.join(allowed_filters) + '.')

    def get_code(self):
        return 10
