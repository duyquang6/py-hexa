import peewee

from src.domain.repository.todolist import ToDoListRepository
from src.domain.entity.task import Task

class ToDoListRepositoryImpl(ToDoListRepository):
    def create_task(self, db: peewee.Database,task: Task):
        # Task.create(
            
        # )
        pass