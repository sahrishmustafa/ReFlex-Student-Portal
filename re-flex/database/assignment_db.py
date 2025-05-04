# database/assignment_db.py

from models.assignment import Assignment

def get_assignments_for_student(student_id):
    return [
        Assignment("CS101", "Assignment 2", "2025-05-05"),
        Assignment("MA102", "Homework 1", "2025-05-08")
    ]
