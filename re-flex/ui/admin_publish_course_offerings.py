from datetime       import datetime
from pywebio.input  import textarea, input, NUMBER, input_group, select
from pywebio.output import put_markdown, put_text, put_table, put_buttons, clear, put_error

from database.course_db import insert_course
from database.section_db import insert_section

def handle_publish_offerings(semester_number, back_to_dashboard, user_email):
    """Allow multiple course offerings for a semester until user exits."""
    while True:
        clear()
        put_markdown(f"### 📢 Publish Course Offering: Semester {semester_number} (by {user_email})")

        # Input for course details
        while True:
            try:
                course_data = input_group("📘 Enter Course Details", [
                    input('Course ID', name='courseid', required=True),
                    input('Course Title', name='title', required=True),
                    input('Credit Hours', name='credithours', type=NUMBER, required=True),
                    textarea('Course Description', name='description', rows=3, required=True)
                ])

                # Custom validation
                if not course_data['courseid'].strip():
                    raise ValueError("Course ID cannot be empty.")

                if not course_data['title'].strip():
                    raise ValueError("Course Title cannot be empty.")

                if course_data['credithours'] <= 0:
                    raise ValueError("Credit Hours must be a positive number.")

                if not course_data['description'].strip():
                    raise ValueError("Course Description cannot be empty.")

                break  # ✅ Valid input, exit loop

            except ValueError as ve:
                put_error(f"❌ Input Error: {ve}. Please correct and try again.")

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

    put_buttons(['🔙 Back to Dashboard'], onclick=[lambda: back_to_dashboard(user_email)])
