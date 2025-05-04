# database/attendance_db.py

from models.attendance import Attendance

def get_attendance_records(student_id):
    return [
        Attendance("CS101", 92),
        Attendance("MA102", 88)
    ]
