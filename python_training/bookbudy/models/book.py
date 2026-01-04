#  Book Object
from datetime import datetime

class Book:
    counter = 0

    def __init__(self, title: str, author: str, genre: str, pages: int, date_added: datetime):
        self.title = title
        self.author = author
        self.genre = genre
        self.pages = pages
        self.date_added = date_added
        self.is_ended = False
        Book.counter += 1

    def __str__(self):
        return "%s by %s . this genre %s and have a %s you %s "  % (self.title, self.author, self.genre, self.pages, f'{"end him " if self.is_ended else "dont end him"}')

    def __repr__(self):
        return f"Book(title='{self.title}', author='{self.author}', genre='{self.genre}', pages={self.pages}, date_added={self.date_added}, is_ended={self.is_ended})"

    def __eq__(self, other):
        return self.title == other.title

    def change_status(self, read_pages: int) -> bool:
        if self.pages <= read_pages:
            self.is_ended = True
            return self.is_ended

        return self.is_ended

if __name__ == "__main__":
    b = Book(title="ars",author="ars", genre="sdfsd", pages=1, date_added=datetime.now().strftime("%d/%m/%Y, %H:%M:%S"))
    test = b.__dict__.get("title", "")

    print(test)
