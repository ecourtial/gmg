import threading
from typing import Any

from mysql import connector


class MySQLFactory:
    _local: threading.local = threading.local()

    @classmethod
    def init(cls, host: str, user: str, password: str, database: str) -> None:
        cls._host = host
        cls._user = user
        cls._password = password
        cls._database = database

    @classmethod
    def get(cls) -> Any:
        """Get a thread-local connection, creating or reconnecting if needed."""
        conn = getattr(cls._local, 'connection', None)
        if conn is None:
            conn = connector.connect(
                host=cls._host,
                user=cls._user,
                passwd=cls._password,
                database=cls._database
            )
            cls._local.connection = conn
        else:
            conn.ping(reconnect=True)

        return conn

    @classmethod
    def close(cls) -> None:
        conn = getattr(cls._local, 'connection', None)
        if conn is not None:
            conn.close()
            cls._local.connection = None
