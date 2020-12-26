from dataclasses import dataclass
from datetime import datetime
from dataclasses_json import dataclass_json, LetterCase


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass(frozen=True)
class Meta:
    code: int = 0
    message: str = ''
