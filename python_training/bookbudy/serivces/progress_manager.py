from .reading_tracker import ReadingTracker
from models.book import Book
from typing import Dict, List, Any

class ProgressManager:
    def __init__(self, tracker: ReadingTracker):
        self.tracker = tracker

    def calculate_pages(self, book:Book) -> Dict[str, Any]:
        result = self.tracker.get_book_read_log(book.title)
        page_read = sum(r.book_page for r in result)

        if book.change_status(page_read):
            page_read = book.pages

        percent_up = (page_read / book.pages ) * 100

        return {"page_read": page_read, "percent": percent_up, "is_ended": book.is_ended}