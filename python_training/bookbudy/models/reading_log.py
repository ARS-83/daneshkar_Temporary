from  dataclasses import dataclass, field
from datetime import datetime

@dataclass
class ReadingLog:
    book_title: str
    book_page: int
    notes: str = ""
    date_read: datetime = field(default_factory=datetime.now())

    def __str__(self):
        return "Book Is %s You Read %d Pages In %s" % (self.book_title, self.book_page, self.date_read.strftime("%Y-%m-%d"))
