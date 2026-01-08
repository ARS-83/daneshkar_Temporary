import pickle

import pickle
from pathlib import Path


class PickleHandlerException(Exception):
    pass


class PickleHandler(object):
    def __init__(self, base_dir: str) -> None:
        self.basedir = Path(base_dir)
        self.basedir.mkdir(exist_ok=True)

    def save(self, data: dict, filename: str) -> None:
        try:
            if not filename.endswith(".pkl"):
                filename += ".pkl"

            path = self.basedir / filename

            with open(path, "wb") as f:
                pickle.dump(data, f)

        except KeyError:
            raise PickleHandlerException("Have bad data")

        except FileNotFoundError:
            raise PickleHandlerException("Error when finding for saVE")

        except Exception:
            raise PickleHandlerException("Error in save")

    def load(self, filename: str) -> dict:
        try:
            if not filename.endswith(".pkl"):
                filename += ".pkl"

            path = self.basedir / filename

            with open(path, "rb") as f:
                data = pickle.load(f)

            if "books" not in data or "logs" not in data:
                raise PickleHandlerException("Have bad data")

            return data

        except FileNotFoundError:
            raise PickleHandlerException("File not found")

        except Exception:
            raise PickleHandlerException("Error in load")
