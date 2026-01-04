from .book import Book


class Ebook(Book):
    _download_link: str = "https://media1.tenor.com/m/U8qmomzRKcoAAAAd/cat-cat-dancing.gif"

    def __init__(self, title: str, author: str, genre: str, pages: int, date_added, file_size: float, file_format: str, download_link: str = ""):
        super().__init__(title, author, genre, pages, date_added)
        self.file_size = file_size  # in MB
        self.file_format = file_format  # e.g., PDF, EPUB
        self.download_link = download_link if download_link else Ebook._download_link

    def __str__(self):
        return super().__str__() + f" [{self.file_format} - {self.file_size}MB]"