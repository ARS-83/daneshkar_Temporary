from datetime import datetime
from print_color import print as cprint

from models.book import Book
from models.ebook import Ebook
from models.audiobook import Audiobook
from models.reading_log import ReadingLog

from serivces.reading_tracker import ReadingTracker, ReadingTrackerError
from serivces.progress_manager import ProgressManager

from storage.data_exporter import Exporter, ExporterError
from storage.json_handler import JsonHandlerException
from storage.pickle_handler import PickleHandlerException


data = dict(books=list(), logs=list())

tracker = ReadingTracker()
progress_manager = ProgressManager(tracker)

exporter = Exporter()


def add_book():
    cprint("\nAdd a New Book", color="cyan")
    cprint("1. Book", color="yellow")
    cprint("2. EBook", color="yellow")
    cprint("3. AudioBook", color="yellow")

    t = input("Select book type (1-3): ").strip()

    title = input("Enter book title: ").strip()
    author = input("Enter author name: ").strip()
    genre = input("Enter genre: ").strip()
    pages = int(input("Enter total pages: ").strip())
    date_added = datetime.now()

    if t == "1":
        book = Book(title, author, genre, pages, date_added)
        data["books"].append(book)
        cprint(f"\nBook '{title}' added successfully!", color="green")

    elif t == "2":
        file_size = float(input("Enter file size (MB): ").strip())
        file_format = input("Enter file format (PDF/EPUB/...): ").strip()
        download_link = input("Enter download link (optional): ").strip()

        book = Ebook(title, author, genre, pages, date_added, file_size, file_format, download_link)
        data["books"].append(book)
        cprint(f"\nEBook '{title}' added successfully!", color="green")

    elif t == "3":
        duration = int(input("Enter duration (minutes): ").strip())
        narrator = input("Enter narrator name: ").strip()
        sample_link = input("Enter sample audio link (optional): ").strip()

        book = Audiobook(title, author, genre, pages, date_added, duration, narrator, sample_link)
        data["books"].append(book)
        cprint(f"\nAudioBook '{title}' added successfully!", color="green")

    else:
        cprint("\nInvalid book type. Please try again.", color="red")


def view_books():
    cprint("\nYour Library", color="cyan")

    if len(data["books"]) == 0:
        cprint("No books added yet.", color="yellow")
        return

    for i, book in enumerate(data["books"], start=1):
        cprint(f"{i}. {book}", color="white")


def log_reading():
    cprint("\nLog Reading Progress", color="cyan")

    if len(data["books"]) == 0:
        cprint("No books available. Please add a book first.", color="yellow")
        return

    title = input("Enter book title: ").strip()
    pages_read = int(input("Enter pages read: ").strip())
    notes = input("Enter notes (optional): ").strip()

    log = ReadingLog(book_title=title, book_page=pages_read, notes=notes, date_read=datetime.now())

    tracker.add_log(log)
    tracker.logs.append(log)
    data["logs"].append(log)

    cprint("\nReading progress logged successfully!", color="green")


def view_progress():
    cprint("\nReading Progress", color="cyan")

    if len(data["books"]) == 0:
        cprint("No books available. Please add a book first.", color="yellow")
        return

    if len(data["logs"]) == 0:
        cprint("No reading logs found. Please log your reading first.", color="yellow")
        return

    for book in data["books"]:
        p = progress_manager.calculate_pages(book)

        status = "Completed" if p["is_ended"] else "In Progress"
        color = "green" if p["is_ended"] else "yellow"

        cprint(
            f"- {book.title}: {p['page_read']}/{book.pages} pages ({p['percent']:.1f}%) | Status: {status}",
            color=color
        )


def export_data():
    cprint("\nExport Book Data", color="cyan")
    cprint("1. JSON", color="yellow")
    cprint("2. Pickle", color="yellow")

    t = input("Select export format (1-2): ").strip()

    if t not in ("1", "2"):
        cprint("\nInvalid format. Please try again.", color="red")
        return

    chose = int(t)

    exporter.export(data, chose)

    if chose == 1:
        cprint("\nData exported successfully to 'data/data.json'.", color="green")
    else:
        cprint("\nData exported successfully to 'data/data.pk1.pkl'.", color="green")


def import_data():
    cprint("\nImport Book Data", color="cyan")
    cprint("1. JSON", color="yellow")
    cprint("2. Pickle", color="yellow")

    t = input("Select import format (1-2): ").strip()

    if t not in ("1", "2"):
        cprint("\nInvalid format. Please try again.", color="red")
        return

    filename = input("Enter filename (with extension): ").strip()
    chose = int(t)

    global data
    data = exporter.import_data(filename, chose)

    tracker.logs = []
    for log in data["logs"]:
        tracker.logs.append(log)

    cprint(f"\nData imported successfully from '{filename}'.", color="green")


def main():
    cprint("Welcome to BookBuddy!", color="magenta")
    cprint("Track your reading, log progress, and manage your personal library.", color="white")

    while True:
        cprint("\nMain Menu", color="cyan")
        cprint("1. Add a new book", color="yellow")
        cprint("2. View all books", color="yellow")
        cprint("3. Log reading progress", color="yellow")
        cprint("4. View reading progress", color="yellow")
        cprint("5. Export book data", color="yellow")
        cprint("6. Import book data", color="yellow")
        cprint("7. Exit", color="yellow")

        choice = input("Enter your choice (1-7): ").strip()

        try:
            if choice == "1":
                add_book()

            elif choice == "2":
                view_books()

            elif choice == "3":
                log_reading()

            elif choice == "4":
                view_progress()

            elif choice == "5":
                export_data()

            elif choice == "6":
                import_data()

            elif choice == "7":
                cprint("\nGoodbye! See you next time.", color="magenta")
                break

            else:
                cprint("\nInvalid choice. Please enter a number from 1 to 7.", color="red")

        except (ValueError, ReadingTrackerError, ExporterError, JsonHandlerException, PickleHandlerException) as e:
            cprint(f"\nError: {e}", color="red")


if __name__ == "__main__":
    main()
