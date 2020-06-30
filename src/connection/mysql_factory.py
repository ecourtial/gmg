from mysql import connector

class MySQLFactory:
    
    @classmethod
    def init(cls, host, user, password, database):
        cls.host = host
        cls.user = user
        cls.password = password
        cls.database = database
        cls.connection = None

    @classmethod
    def get(cls):
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
    def close(cls):
        if cls.connection is not None:
            cls.connection.close()
            cls.connection = None