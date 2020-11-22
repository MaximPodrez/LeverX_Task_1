class Merger:

    def __init__(self, rooms: list, students: list) -> None:
        self.rooms = rooms
        self.students = students
        self.rooms_with_students = {}
        self._fill_rooms_with_students()
        self.merge()

    def _fill_rooms_with_students(self) -> None:
        for room in self.rooms:
            self.rooms_with_students[str(room['id'])] = {
                'name': room['name'],
                'students': {}
            }

    def merge(self) -> None:
        for student in self.students:
            self.rooms_with_students[str(student['room'])]['students'][str(student['id'])] = {
                'name': student['name']
            }
