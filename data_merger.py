class RoomsStudentsMerger:

    def __init__(self, rooms: list, students: list) -> None:
        self.rooms = rooms
        self.students = students
        self.rooms_with_students = {}

    def _fill_rooms_with_students(self) -> None:
        for room in self.rooms:
            self.rooms_with_students[str(room['id'])] = {
                'name': room['name'],
                'students': {}
            }

    def merge(self) -> dict:
        self._fill_rooms_with_students()
        for student in self.students:
            room = self.rooms_with_students[str(student['room'])]
            room['students'][str(student['id'])] = {
                'name': student['name']
            }
        return self.rooms_with_students
