import json
from abc import ABC, abstractmethod
from xml.dom.minidom import parseString
from dicttoxml import dicttoxml


class Writer(ABC):

    @abstractmethod
    def write(self, data: dict, path: str) -> None:
        pass


class WriterJSON(Writer):

    def write(self, data: dict, path: str) -> None:
        with open(path + 'rooms_with_students.json', 'w') as file:
            json.dump(data, file, indent=4)


class WriterXML(Writer):

    def write(self, data: dict, path: str) -> None:
        xml = dicttoxml(data, custom_root='rooms', attr_type=False).decode()
        pretty_xml_as_string = parseString(xml).toprettyxml()
        with open(path + 'rooms_with_students.xml', 'w') as file:
            file.write(pretty_xml_as_string)
