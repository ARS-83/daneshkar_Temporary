from utils import decorators
from models.reading_log import ReadingLog
from typing import List

class ReadingTrackerError(Exception):
    pass

class ReadingTracker:
    def __init__(self,) -> None:
        self.logs: List[ReadingLog] = []

    def __str__(self):
        return "Manager Your Tracker."

    def add_log(self, log:ReadingLog) -> List[ReadingLog]:
        if log.book_page <= 0:
            raise ReadingTrackerError("Pages read must be grater than 0")

    def get_book_read_log(self, book_title: str) -> List[ReadingLog]:
        return [log for log in self.logs if log.book_title.strip().lower() == book_title.strip().lower()]

