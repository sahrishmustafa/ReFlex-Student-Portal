from pywebio.output import put_text, put_table, put_buttons, clear, put_markdown
from database.student_db import get_student_grades

def view_marks_and_grades(email,return_dashboard):
    clear()
    put_markdown(f"### 📊 Grades for: `{email}`")
    
    grades_table = get_student_grades(email)
    put_table(grades_table)

    put_buttons(['🔙 Back to Dashboard'], [lambda: return_dashboard(email)])
