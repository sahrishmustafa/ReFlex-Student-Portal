from pywebio.input import select, actions
from pywebio.output import put_markdown, put_buttons, put_text, toast, clear
from database.student_db import get_registered_courses_for_student, drop_course 

def drop_courses(user_email, go_back_callback):
    clear()
    put_markdown(f"## ❌ Drop Registered Course")

    courses = get_registered_courses_for_student(user_email)

    if not courses:
        put_text("You have no registered courses to drop.")
    else:
        course_id = select("Select a course to drop:", options=[
            f"{course[0]} - {course[1]} {course[2]}" for course in courses
        ])

        result = actions("Are you sure you want to drop this course?", buttons=[
            {'label': 'Yes, Drop', 'value': 'drop'},
            {'label': 'Cancel', 'value': 'cancel'}
        ])

        if result == 'drop':
            drop_course(user_email, course_id)
            toast("✅ Course dropped successfully.")
        else:
            toast("❌ Drop cancelled.")

    put_buttons(['Back to Dashboard'], onclick=[lambda: go_back_callback(user_email)])
