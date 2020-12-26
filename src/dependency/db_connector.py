import peewee


def connect_sqlite_db(database_uri):
    db = peewee.SqliteDatabase(database_uri)    
    yield db
    db.close()