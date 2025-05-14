from pywebio.input import input, file_upload
from pywebio.output import put_text, put_table, put_buttons, put_markdown, clear


def faculty_dashboard(faculty_email):
    from ui import faculty_upload_assignments, faculty_enter_grades, faculty_mark_attendance, faculty_upload_material, faculty_answer_queries
    from database.faculty_db import get_faculty_id_by_email

    faculty_id = faculty_email if isinstance(faculty_email, int) else int(get_faculty_id_by_email(faculty_email))

    clear()
    put_markdown('# 👨‍🏫 Faculty Dashboard')
    put_buttons(
        ['Upload Assignments', 'Enter Grades', 'Mark Attendance', 
         'Upload Materials', 'Answer Queries'],
        
        onclick = [
            lambda: faculty_upload_assignments.upload_assignments(faculty_dashboard, faculty_id),
            lambda: faculty_enter_grades.enter_student_grades(faculty_dashboard, faculty_id),
            lambda: faculty_mark_attendance.mark_attendance(faculty_dashboard, faculty_id),
            lambda: faculty_upload_material.upload_course_materials(faculty_dashboard, faculty_id),
            lambda: faculty_answer_queries.respond_student_queries(faculty_dashboard, faculty_id)
        ]

    )
