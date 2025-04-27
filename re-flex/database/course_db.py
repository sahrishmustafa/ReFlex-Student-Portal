# database/course_db.py

from models.course import Course

def get_registered_courses(student_id):
    # Dummy hardcoded courses
    return [
        Course("CS101", "Introduction to Programming"),
        Course("MA102", "Calculus I")
    ]
