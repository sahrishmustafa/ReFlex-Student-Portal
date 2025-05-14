from pywebio.input import select, textarea
from pywebio.output import put_markdown, toast, put_buttons, clear

from database.student_db import get_student_id_by_email
from database.studentquery_db import insert_student_query
from database.faculty_db import get_faculty_by_course_section
from database.student_db import get_registered_courses_for_student

def communicate_with_teacher(student_email, go_back_callback):
    clear()
    put_markdown("## 📨 Contact Your Teacher")

    COURSE_DATA = get_registered_courses_for_student(student_email)

    if not COURSE_DATA:
        toast("⚠️ No enrolled courses found.")
        return

    # Build display-friendly course options: "CS101 - Intro to CS"
    course_options = [
        f"{course[0]} - {course[1]}" for course in COURSE_DATA[1:]
    ]

    course_code_to_section = {course[0]: course[2] for course in COURSE_DATA}

    # Select a course from the options
    selected_option = select("Select Course", options=course_options)

    # Extract course code from selected option
    selected_course = selected_option.split(" - ")[0]
    selected_section = course_code_to_section[selected_course]

    # Message area
    message_text = textarea(
        "Message to Teacher",
        placeholder="Write your question or message here...",
        rows=6
    )

    if message_text.strip():
        faculty_id = get_faculty_by_course_section(selected_course, selected_section)
        student_id = get_student_id_by_email(student_email)
        insert_student_query(faculty_id, student_id, selected_course, selected_section, message_text)
        toast("✅ Your message was sent to the teacher.")
    else:
        toast("⚠️ Please write a message before submitting.")

    # Back/refresh buttons
    put_buttons(['🔄 Send Another', '🏠 Back to Dashboard'], onclick=[
        lambda: communicate_with_teacher(student_email, go_back_callback),
        lambda: go_back_callback(student_email)
    ])

