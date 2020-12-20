from abc import ABC, abstractmethod

class ToDoListRepository(ABC):
    @abstractmethod
    def create_task(self, purchase):
        pass