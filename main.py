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

read_registry = {
    DataType.JSON: ReaderJSON,
}


def start(students_path, rooms_path, file_format):
    reader_class = read_registry.get('json')
    reader = reader_class()
    students = reader.read(students_path)
    rooms = reader.read(rooms_path)
    merger = RoomsStudentsMerger(rooms, students)
    result = merger.merge()
    writer_class = writer_registry.get(file_format)
    if writer_class is None:
        print('Incorrect format!')
    else:
        writer = writer_class()
        writer.write(result, '')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Merge rooms and students script')
    parser.add_argument('-students', action="store", dest="students")
    parser.add_argument('-rooms', action="store", dest="rooms")
    parser.add_argument('-format', action="store", dest="format")
    args = parser.parse_args()
    start(args.students, args.rooms, args.format)
