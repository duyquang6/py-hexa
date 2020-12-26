from dataclasses import dataclass
from datetime import datetime
from dataclasses_json import dataclass_json, LetterCase
import peewee

from .base import BaseModel


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass(frozen=True)
class ToDoList(BaseModel):    
    title: str
    author: str