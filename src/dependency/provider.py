from dependency_injector import containers, providers
from .db_connector import connect_sqlite_db

container = None
class Container(containers.DeclarativeContainer):

    config = providers.Configuration()

    db_client = providers.Singleton(
        connect_sqlite_db,
        database_uri=config.DATABASE_NAME()
    )

if not container:
    container = Container()