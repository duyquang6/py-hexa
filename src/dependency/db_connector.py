import peewee


def connect_sqlite_db(database_uri):
    db = peewee.SqliteDatabase(database_uri)    
    return db