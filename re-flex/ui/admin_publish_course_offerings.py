from datetime       import datetime
from pywebio.input  import textarea, input, NUMBER, input_group, select
from pywebio.output import put_markdown, put_text, put_table, put_buttons, clear

from database.course_db import insert_course
from database.section_db import insert_section

def handle_publish_offerings(semester_number, back_to_dashboard, user_email):
    """Allow multiple course offerings for a semester until user exits."""
    while True:
        clear()
        put_markdown(f"### 📢 Publish Course Offering: Semester {semester_number} (by {user_email})")

        # Input for course details
        course_data = input_group("📘 Enter Course Details", [
            input('Course ID', name='courseid'),
            input('Course Title', name='title'),
            input('Credit Hours', name='credithours', type=NUMBER),
            textarea('Course Description', name='description', rows=3)
        ])

        courseid     = course_data['courseid']
        title        = course_data['title']
        credithours  = course_data['credithours']
        description  = course_data['description']

        # Insert course with semester info
        insert_course(courseid, title, credithours, description, semester_number)

        # Input section info (multiple sections optional)
        while True:
            section_data = input_group("➕ Add Section", [
                input('Section ID (e.g., A, B1)', name='sectionid'),
                input('Student Strength', type=NUMBER, name='student_strength')
            ])

            sectionid = section_data['sectionid']
            student_strength = section_data['student_strength']

            insert_section(sectionid, courseid, student_strength)
            put_text(f"Section {sectionid} added for {courseid}.")

            section_next = select("Add another section for this course?", ['Yes', 'No'])
            if section_next != 'Yes':   break

        put_text(f"Course {courseid} and its sections added successfully.")

        result = select("Add another course for this course?", ['Yes', 'No'])
        if result != 'Yes': break

    # Return to dashboard or offerings
    clear()
    put_text("🔙 Returning to course offerings page...")
    publish_course_offerings(back_to_dashboard, user_email)

def publish_course_offerings(back_to_dashboard, user_email):
    """Dashboard listing semester numbers with publish actions."""
    clear()
    put_markdown('# 🎓 Publish Course Offerings')
    rows = []
    for semester_number in range(1, 9):  
        rows.append([
            f"Semester {semester_number}",
            put_buttons(['Publish'], onclick=[
                lambda s=semester_number: handle_publish_offerings(s, back_to_dashboard, user_email)
            ])
        ])
    put_table([['Semester', 'Course'], *rows])
