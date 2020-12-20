import peewee
import inject
from abc import ABC, abstractmethod

@inject.autoparams()
def connect_sqlite_db(database_uri):
    db = peewee.SqliteDatabase(database_uri)
    db.connect()
    db.execute_sql()
    return peewee.SqliteDatabase(database_uri)


class DatabaseInterface(ABC):
    @abstractmethod
    def beginTx(self):
        pass

    @abstractmethod
    def commitTx(self):
        pass

class SQLiteAdapter(DatabaseInterface):
    def beginTx(self):
        pass
    pass