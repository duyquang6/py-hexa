from pydantic import BaseSettings


class Settings(BaseSettings):
    app_name: str = "ToDoList FastAPI"        
    database_uri: str = 'todolist.db'

settings = Settings()