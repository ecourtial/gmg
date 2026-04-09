from typing import Any


class AbstractCoreRepository:  # pylint: disable=no-member
    """Another useless comment"""
    def __init__(self, mysql: Any) -> None:
        self.mysql = mysql

    def fetch_one(self, request: str, data_tuple: tuple[Any, ...]) -> Any:
        """Fetch one result from a given request."""
        cursor = self.mysql.cursor(dictionary=True)
        cursor.execute(request, data_tuple)
        row = cursor.fetchone()

        if row is None:
            return None

        hydrated = self.hydrate(row)
        cursor.close()

        return hydrated

    def fetch_multiple(self, request: str, data_tuple: tuple[Any, ...]) -> list[Any]:
        """Fetch mutliple items and return a list."""
        items_list = []
        cursor = self.mysql.cursor(dictionary=True, buffered=True)
        cursor.execute(request, data_tuple)

        while True:
            row = cursor.fetchone()
            if row is None:
                break
            items_list.append(self.hydrate(row))

        cursor.close()
        return items_list

    def hydrate(self, row: dict[str, Any]) -> Any:
        """Hydrate an object from a row."""
        values = []
        values.append(row[self.entity.primary_key])

        for api_field, data in self.entity.expected_fields.items():  # pylint: disable=W0612
            values.append(row[data['field']])

        object = self.entity(*values)

        return object

    def write(self, request: str, data: list[Any] | tuple[Any, ...], commit: bool = True) -> int | None:
        """Performs an UPDATE or WRITE statement"""
        cursor = self.mysql.cursor()
        cursor.execute(request, data)

        if commit:
            self.mysql.commit()
        else:
            self.mysql.autocommit = False

        return cursor.lastrowid

    def fetch_cursor(self, request: str, data_tuple: list[Any] | dict[str, Any] | None = None) -> dict[str, Any] | None:
        """Fetch one result"""
        if data_tuple is None:
            data_tuple = {}

        cursor = self.mysql.cursor(dictionary=True)
        cursor.execute(request, data_tuple)
        row = cursor.fetchone()
        cursor.close()

        return row
