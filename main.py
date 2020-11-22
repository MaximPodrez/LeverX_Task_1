import sys
from DataLoader import LoaderXML, LoaderJSON
from DataMerger import Merger
from DataParser import ParserJSON


class DataType:
    JSON = 'json'
    XML = 'xml'


loaders_registry = {
    DataType.JSON: LoaderJSON,
    DataType.XML: LoaderXML,
}


def start(students_path, rooms_path, file_format):
    parser = ParserJSON(students_path, rooms_path)
    merger = Merger(parser.rooms, parser.students)
    loader_class = loaders_registry.get(file_format)
    if loader_class is None:
        print('Incorrect format!')
    else:
        loader = loader_class(merger.rooms_with_students, '')
        loader.load()


if __name__ == '__main__':
    start(sys.argv[1], sys.argv[2], sys.argv[3])
