import json
from abc import ABC, abstractmethod
from xml.dom.minidom import parseString
from dicttoxml import dicttoxml


class Writer(ABC):

    def __init__(self, data: dict, path: str) -> None:
        self.data = data
        self.path = path

    @abstractmethod
    def write(self) -> None:
        pass


class WriterJSON(Writer):

    def write(self) -> None:
        with open(self.path + 'rooms_with_students.json', 'w') as file:
            json.dump(self.data, file, indent=4)


class WriterXML(Writer):

    def write(self) -> None:
        xml = dicttoxml(self.data, custom_root='rooms', attr_type=False).decode()
        pretty_xml_as_string = parseString(xml).toprettyxml()
        with open(self.path + 'rooms_with_students.xml', 'w') as file:
            file.write(pretty_xml_as_string)
