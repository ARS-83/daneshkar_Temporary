from  dataclasses import dataclass, field
from datetime import datetime
from typing import Union

@dataclass
class ReadingLog:
    book_title: str
    book_page: int
    notes: str = ""
    date_read: Union[str, datetime] = field(default_factory=datetime.now)

    def __post_init__(self):
        if isinstance(self.date_read, datetime):
            self.date_read = self.date_read.strftime("%d-%m-%Y,  %H:%M:%S")

    def __str__(self):
        return f"Book is {self.book_title} | You read {self.book_page} pages | Date: {self.date_read}"