import json
from abc import ABC, abstractmethod
from xml.dom.minidom import parseString
from dicttoxml import dicttoxml


class Loader(ABC):

    def __init__(self, data: dict, path: str) -> None:
        self.data = data
        self.path = path

    @abstractmethod
    def load(self) -> None:
        pass


class LoaderJSON(Loader):

    def load(self) -> None:
        with open(self.path + 'rooms_with_students.json', 'w') as file:
            json.dump(self.data, file, indent=4)


class LoaderXML(Loader):

    def load(self) -> None:
        xml = dicttoxml(self.data, custom_root='rooms', attr_type=False).decode()
        pretty_xml_as_string = parseString(xml).toprettyxml()
        with open(self.path + 'rooms_with_students.xml', 'w') as file:
            file.write(pretty_xml_as_string)
