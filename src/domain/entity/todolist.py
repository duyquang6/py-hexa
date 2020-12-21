from dataclasses import dataclass
from datetime import datetime
from dataclasses_json import dataclass_json, LetterCase

from .base import BaseModel


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass(frozen=True)
class ToDoList(BaseModel):
    id: int
    author: str    
    created_at: datetime
    updated_at: datetime