# database/student_db.py

from models.student import Student

def get_student_by_id(student_id):
    # Dummy hardcoded student
    return Student(student_id, "John Doe", "john@example.com")
