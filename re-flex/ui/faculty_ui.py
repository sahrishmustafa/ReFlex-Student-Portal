from pywebio.output import put_text, put_table, put_buttons, put_markdown, clear
from pywebio.input import input, file_upload

def faculty_dashboard(user_email):
    from ui import faculty_upload_assignments, faculty_enter_grades, faculty_mark_attendance, faculty_upload_material, faculty_answer_queries

    clear()
    put_markdown('# 👨‍🏫 Faculty Dashboard')
    put_markdown(f"# 👨‍🏫 Faculty Dashboard ({user_email})")
    put_buttons(
        ['Upload Assignments', 'Enter Grades', 'Mark Attendance', 
         'Upload Materials', 'Answer Queries'],
        onclick=[
            lambda: faculty_upload_assignments.upload_assignments(faculty_dashboard),
            lambda: faculty_enter_grades.enter_student_grades(faculty_dashboard),
            lambda: faculty_mark_attendance.mark_attendance(faculty_dashboard),
            lambda: faculty_upload_material.upload_course_materials(faculty_dashboard),
            lambda: faculty_answer_queries.respond_student_queries(faculty_dashboard)
        ]
    )
