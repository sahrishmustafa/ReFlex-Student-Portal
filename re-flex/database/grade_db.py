# database/grade_db.py

from models.grade import Grade

def get_grades(student_id):
    return [
        Grade("CS101", "Assignment 1", 85),
        Grade("CS101", "Quiz 1", 78),
        Grade("MA102", "Midterm Exam", 90)
    ]
