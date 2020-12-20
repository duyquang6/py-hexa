from dataclasses import dataclass
from datetime import datetime

from dataclasses_json import dataclass_json, LetterCase


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass(frozen=True)
class Task:
    id: int    
    title: str
    body: str    
    expired_at: datetime
    created_at: datetime
    updated_at: datetime