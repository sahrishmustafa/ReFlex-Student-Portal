from pywebio.input import select, actions
from pywebio.output import put_text, put_buttons, put_markdown, toast, clear, put_table

from database.student_db import get_student_semester
from database.student_db import register_student_to_course
from database.course_db import get_available_courses_with_sections

def course_registration(user_email, go_back_callback):
    clear()
    put_markdown(f"## 📚 Course Registration for {user_email}")
    
    # Step 1: Get available courses from the DB (dummy function)
    current_semester = get_student_semester(user_email)
    available_courses = get_available_courses_with_sections(current_semester)
    
    if not available_courses:
        put_text("No courses available for registration at the moment.")
        put_buttons(['Back to Dashboard'], onclick=[lambda: go_back_callback(user_email)])
        return

    put_table([
        ['Course ID', 'Title', 'Credit Hours', 'Description', 'Section', 'Strength'],
        *[
            [course[0], course[1], course[2], course[3], course[4], course[5]]
            for course in available_courses
        ]
    ])

    # Create selection options: "CS101 - Intro to CS (Section A)"
    course_section_options = [
        f"{course[0]} - {course[1]} (Section {course[4]})" for course in available_courses
    ]

    # Let user select course and section
    selected = select("Select a course and section to register:", options=course_section_options)

    # Step 3: Confirm registration
    result = actions("Do you want to register for this course section?", buttons=[
        {'label': 'Register', 'value': 'register'},
        {'label': 'Cancel', 'value': 'cancel'}
    ])
    
    if result == 'register':
        if " (" in selected and ")" in selected:
            # Extract course ID (before " - ")
            course_id = selected.split(" - ")[0]
            section_id = selected.split("(")[1].split(")")[0].strip().split()[-1]

            register_student_to_course(user_email, course_id, section_id)
    else:
        toast("❌ Registration canceled")

    # Step 4: Return option
    put_buttons(['Back to Dashboard'], onclick=[lambda: go_back_callback(user_email)])
