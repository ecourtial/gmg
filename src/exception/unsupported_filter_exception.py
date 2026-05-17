class UnsupportedFilterException(Exception):
    def __init__(self, field: str, allowed_filters: list[str]) -> None:
        super().__init__(f"The following filter is not allowed: {field}. Allowed filters are: " + ', '.join(allowed_filters) + '.')

    def get_code(self) -> int:
        return 10
