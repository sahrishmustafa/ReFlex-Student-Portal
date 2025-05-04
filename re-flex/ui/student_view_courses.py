from pywebio.output import put_text, put_table, put_markdown, put_buttons, clear
from database.student_db import get_registered_courses_for_student

def view_registered_courses(email,return_dashboard):
    clear()
    put_markdown(f'## 📚 Registered Courses for {email}')
    
    courses = get_registered_courses_for_student(email)
    if len(courses) > 1:
        put_table(courses)
    else:
        put_text("You are not registered in any courses.")

    put_buttons(
        ['⬅️ Back to Dashboard'],
        [lambda: return_dashboard(email)]
    )
