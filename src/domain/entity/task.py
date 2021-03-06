from dataclasses import dataclass
from datetime import datetime
from dataclasses_json import dataclass_json, LetterCase
import peewee
from .base import BaseModel
from .todolist import ToDoList


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass(frozen=True)
class Task(BaseModel):
    title: str
    expired_at: datetime
    todolist: ToDoList

