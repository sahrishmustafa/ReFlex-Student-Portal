from pywebio.output import put_text, put_table, put_buttons, put_markdown, clear
from pywebio.input import input, file_upload
from ui.faculty_answer_queries import respond_student_queries
from ui.faculty_enter_grades     import enter_student_grades
from ui.faculty_mark_attendance          import mark_attendance
from ui.faculty_upload_material  import upload_course_materials
from ui.faculty_upload_assignments import upload_assignments

def faculty_dashboard(faculty_id=None):
    """
    Main Faculty Dashboard: displays buttons for all faculty actions.
    """
    clear()
    put_markdown(f"# 👨‍🏫 Faculty Dashboard")
    put_buttons(
        ['Upload Assignments',
         'Enter Student Grades',
         'Mark Attendance',
         'Upload Course Materials',
         'Respond to Student Queries'],
        onclick=[
            lambda: upload_assignments(),
            lambda: enter_student_grades(),
            lambda: mark_attendance(),
            lambda: upload_course_materials(),
            lambda: respond_student_queries()
        ]
    )
