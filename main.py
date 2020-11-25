import argparse
from DataWriter import WriterXML, WriterJSON
from DataMerger import Merger
from DataReader import ReaderJSON


class DataType:
    JSON = 'json'
    XML = 'xml'


loaders_registry = {
    DataType.JSON: WriterJSON,
    DataType.XML: WriterXML,
}


def start(students_path, rooms_path, file_format):
    reader = ReaderJSON(students_path, rooms_path)
    merger = Merger(reader.rooms, reader.students)
    loader_class = loaders_registry.get(file_format)
    if loader_class is None:
        print('Incorrect format!')
    else:
        loader = loader_class(merger.rooms_with_students, '')
        loader.write()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Merge rooms and students script')
    parser.add_argument('-students', action="store", dest="students")
    parser.add_argument('-rooms', action="store", dest="rooms")
    parser.add_argument('-type', action="store", dest="type")
    args = parser.parse_args()
    start(args.students, args.rooms, args.type)
