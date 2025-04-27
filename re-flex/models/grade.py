# models/grade.py

class Grade:
    def __init__(self, course_code, assessment_name, marks):
        self.course_code = course_code
        self.assessment_name = assessment_name
        self.marks = marks
