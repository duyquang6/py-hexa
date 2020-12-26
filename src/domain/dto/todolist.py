from dataclasses import dataclass
from datetime import datetime
from dataclasses_json import dataclass_json, LetterCase
from .meta import Meta

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass(frozen=True)
class CreateToDoListRequest:
    author: str
    title: str


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass(frozen=True)
class CreateToDoListResponse:
    meta: Meta = Meta()