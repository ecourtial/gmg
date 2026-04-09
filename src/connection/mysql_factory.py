from typing import Any

from mysql import connector


class MySQLFactory:

    @classmethod
    def init(cls, host: str, user: str, password: str, database: str) -> None:
        cls.host = host
        cls.user = user
        cls.password = password
        cls.database = database
        cls.connection = None

    @classmethod
    def get(cls) -> Any:
        """Get a connection"""
        if cls.connection is None:
            cls.connection = connector.connect(
                host=cls.host,
                user=cls.user,
                passwd=cls.password,
                database=cls.database
            )

        return cls.connection

    @classmethod
    def close(cls) -> None:
        if cls.connection is not None:
            cls.connection.close()
            cls.connection = None
