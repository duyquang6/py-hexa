from dataclasses import dataclass
from datetime import datetime
from dataclasses_json import dataclass_json, LetterCase
import peewee
from .base import BaseModel


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass(frozen=True)
class Task(BaseModel):
    id: int = peewee.BigIntegerField()
    title: str = peewee.CharField()
    body: str = peewee.CharField()
    expired_at: datetime = peewee.DateTimeField()
    created_at: datetime = peewee.DateTimeField()
    updated_at: datetime = peewee.DateTimeField()
