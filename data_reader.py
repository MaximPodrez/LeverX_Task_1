import json
from abc import ABC, abstractmethod


class Reader(ABC):

    @abstractmethod
    def read(self, path):
        pass


class ReaderJSON(Reader):

    def read(self, path):
        with open(path, 'r') as file:
            return json.load(file)
