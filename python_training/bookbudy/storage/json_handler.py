import json
from typing import Any, Dict
from pathlib import Path
from models.book import Book
from models.audiobook import Audiobook
from models.ebook import Ebook
from configs.logger import logger
from models.reading_log import ReadingLog


class JsonHandlerException(Exception):
    pass

class JsonHandler(object):
    def __init__(self, base_dir: str) -> None:
        self.basedir = Path(base_dir)
        self.basedir.mkdir(exist_ok=True)

    def save(self, data: Dict) -> None:
        res = dict(books=list(), logs=list())
        try:
            res['books'] = [book.__dict__ for book in data['books']]
            res['logs'] = [log.__dict__ for log in data["logs"]]
            file_path = self.basedir / "data.json"
            logger.info("{}".format(str(res)))
            with open(file_path, "w", encoding="utf-8") as f:
                res = json.dumps(res)
                f.write(res)

        except KeyError:
            raise JsonHandlerException("Have bad data")

        except Exception as e:
            raise JsonHandlerException("Error while export date {}".format(str(e)))

    def load(self, filename: str) -> Dict:
        data = dict()
        res = dict(books=list(), logs=list())
        try:
            with open(filename, "r", encoding="utf-8") as f:
                data = json.load(f)

        except Exception as e:
            raise JsonHandlerException(f"Error loading JSON: {e}")

        if "books" in data:
            for book in data["books"]:
                if 'file_size' in book.keys():
                    res['books'].append(Ebook(**book))

                elif 'narrator' in book.keys():
                    res['books'].append(Audiobook(**book))

                else: res['books'].append(Book(**book))

        if "logs" in data:
            for log in data["logs"]:
                res['logs'].append(ReadingLog(**log))

        return res


