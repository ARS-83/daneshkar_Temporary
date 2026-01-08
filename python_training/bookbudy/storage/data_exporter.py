from .json_handler import JsonHandler
from .pickle_handler import PickleHandler
from configs.logger import logger
from pathlib import Path
import os

class ExporterError(Exception):
    pass

class Exporter:
    CHOSE_JSON = (1, 'json')
    CHOSE_PICKLE = (2, 'pk1')

    def __init__(self):
        basedir = Path(os.path.dirname(__file__)).resolve().parent / 'data'
        self.json_handler = JsonHandler(basedir)
        self.pickle_handler = PickleHandler(basedir)

    def export(self, data: dict, chose: int):
        logger.info("Exporting data")
        if chose == self.CHOSE_PICKLE[0]:
            return self.pickle_handler.save(data,'data.pk1')
        else:
            return self.json_handler.save(data)

    def import_data(self, filename: str, chose: int):
        logger.info("Saving data")
        directory =  Path.cwd().resolve()
        if chose == self.CHOSE_PICKLE[0]:
            return self.pickle_handler.load(directory /'data'/filename)
        elif chose == self.CHOSE_JSON[0]:
            return self.json_handler.load(directory /'data'/filename)
        else:
            raise ExporterError("Error bad chose")