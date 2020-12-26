from abc import ABC, abstractmethod
from src.repository.todolist import IToDoListRepository
from src.domain.dto import todolist as dto


class IToDoListService(ABC):
    @abstractmethod
    def create_todo_list(self, request: dto.CreateToDoListRequest):
        pass

class ToDoListService(IToDoListService):
    def __init__(self, todo_repo: IToDoListRepository):
        self.todo_repo = todo_repo

    def create_todo_list(self, request: dto.CreateToDoListRequest):
        print(request)
        return True
        res = self.todo_repo.create_todo_list()
        return res
