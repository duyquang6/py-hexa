from dependency_injector import containers, providers
from .db_connector import connect_sqlite_db
from src.repository.todolist import ToDoListRepository
from src.service.todolist import ToDoListService
from fastapi import FastAPI

container = None


class Container(containers.DeclarativeContainer):
    app = providers.Resource(FastAPI)
    config = providers.Configuration()
    db_client = providers.Resource(
        connect_sqlite_db,
        database_uri=config.DATABASE_NAME()
    )
    todolist_repo = providers.Factory(ToDoListRepository, db=db_client)
    todolist_service = providers.Factory(
        ToDoListService, todo_repo=todolist_repo)


container = Container()
