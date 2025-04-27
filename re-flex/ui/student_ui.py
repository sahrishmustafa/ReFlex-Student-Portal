# ui/student_ui.py

from pywebio.output import put_text, put_table, put_buttons, put_markdown
from pywebio.input import input, file_upload

from database.course_db import get_registered_courses
from database.grade_db import get_grades
from database.attendance_db import get_attendance_records

def student_dashboard(student_id):
    put_markdown(f"# 🎓 Welcome Student {student_id}!")
    
    put_buttons(
        ['View Registered Courses', 'View Grades', 'View Attendance', 'Submit Assignment'],
        onclick=[lambda: view_registered_courses(student_id),
                 lambda: view_grades(student_id),
                 lambda: view_attendance(student_id),
                 lambda: submit_assignment(student_id)]
    )

def view_registered_courses(student_id):
    courses = get_registered_courses(student_id)
    put_markdown("## 📚 Your Registered Courses")
    table_data = [["Course Code", "Course Name"]] + [[c.course_code, c.course_name] for c in courses]
    put_table(table_data)

def view_grades(student_id):
    grades = get_grades(student_id)
    put_markdown("## 📝 Your Grades")
    table_data = [["Course Code", "Assessment", "Marks"]] + [[g.course_code, g.assessment_name, g.marks] for g in grades]
    put_table(table_data)

def view_attendance(student_id):
    attendance = get_attendance_records(student_id)
    put_markdown("## 📋 Your Attendance Record")
    table_data = [["Course Code", "Attendance (%)"]] + [[a.course_code, a.attendance_percent] for a in attendance]
    put_table(table_data)

def submit_assignment(student_id):
    put_markdown("## 📤 Submit Assignment")
    course = input("Enter Course Code (e.g., CS101)")
    assignment_file = file_upload("Upload your Assignment", accept="image/*,application/pdf")
    
    put_text(f"Successfully submitted assignment for {course}!")
