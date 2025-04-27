# models/assignment.py

class Assignment:
    def __init__(self, course_code, assignment_name, due_date):
        self.course_code = course_code
        self.assignment_name = assignment_name
        self.due_date = due_date
