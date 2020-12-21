import peewee
from abc import ABC, abstractmethod

from src.domain.entity.task import Task
class ToDoListRepository(ABC):    
    def create_task(self, db: peewee.Database,task: Task):
        pass