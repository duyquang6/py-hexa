import peewee
from abc import ABC, abstractmethod
import traceback
from src.domain.entity.task import Task
from src.domain.entity.todolist import ToDoList


class IToDoListRepository(ABC):
    def create_todo_list(self, todolist: ToDoList):
        pass


class ToDoListRepository(IToDoListRepository):
    def __init__(self, db: peewee.Database):
        self.db = db

    # def create_task(self, todo_id: int, task: Task):
    #     sql = f"insert into tasks(title, author) values ({todolist.title},{todolist.author})"
    #     self.db.execute_sql()

    def create_todo_list(self, todolist: ToDoList):
        sql = f"insert into todolist(title, author) values ({todolist.title},{todolist.author})"
        try:
            self.db.execute_sql(sql)
        except Exception as e:
            print(traceback.format_exc())
            print("got error when connect db, ", e)
            return False
        else:
            return True
