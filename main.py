import argparse
from data_writer import WriterXML, WriterJSON
from data_merger import RoomsStudentsMerger
from data_reader import ReaderJSON


class DataType:
    JSON = 'json'
    XML = 'xml'


writer_registry = {
    DataType.JSON: WriterJSON,
    DataType.XML: WriterXML,
}


def start(students_path, rooms_path, file_format):
    reader = ReaderJSON(students_path, rooms_path)
    merger = RoomsStudentsMerger(reader.rooms, reader.students)
    result = merger.merge()
    loader_class = writer_registry.get(file_format)
    if loader_class is None:
        print('Incorrect format!')
    else:
        loader = loader_class(result, '')
        loader.write()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Merge rooms and students script')
    parser.add_argument('-students', action="store", dest="students")
    parser.add_argument('-rooms', action="store", dest="rooms")
    parser.add_argument('-format', action="store", dest="format")
    args = parser.parse_args()
    start(args.students, args.rooms, args.format)
