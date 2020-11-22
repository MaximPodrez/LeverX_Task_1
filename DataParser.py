import json
from abc import ABC, abstractmethod


class Parser(ABC):

    def __init__(self, students_path: str, rooms_path: str):
        self.students_path = students_path
        self.rooms_path = rooms_path
        self.rooms = None
        self.students = None
        self.upload()

    @abstractmethod
    def upload(self):
        pass


class ParserJSON(Parser):

    def upload(self):
        with open(self.rooms_path, 'r') as room_file:
            self.rooms = json.load(room_file)
        with open(self.students_path, 'r') as student_file:
            self.students = json.load(student_file)
