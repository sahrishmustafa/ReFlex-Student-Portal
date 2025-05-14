from datetime         import date
from pywebio.input    import input, select, input_group
from pywebio.output   import put_markdown, put_text, put_buttons, put_table, clear

from database.course_db import get_faculty_courses_and_sections
from database.course_db import get_students_in_sections
from database.attendance_db import insert_attendance

def handle_mark_attendance(course, section, back_to_dashboard, faculty_id):
    # Mark present/absent for one lecture, then show confirmation.
    put_markdown(f"### 🗓️ Mark Attendance for {course} (Sec {section})")
    
    # Fetch list of students in the course and section
    STUDENTS = get_students_in_sections(course)
    students_in_section = STUDENTS.get(course, {}).get(section, [])
    
    if not students_in_section:
        put_text("No students found in this section.")
        return
    
    # Input for lecture date (using PyWebIO's `input` with `type="date"`)
    lecture_date = input("Enter the lecture date", type="date")
    
    # Create a list of form fields for attendance status
    form_fields = []
    for student in students_in_section:
        # Add a select field for each student to choose attendance status
        form_fields.append(
            select(f"Attendance for {student}", ['Present', 'Absent', 'Late'], name=f'{student}_attendance')
        )

    # Create a form to collect all attendance status selections
    form_data = input_group("Mark Attendance", form_fields)

    # Process each student's attendance selection and insert it into the database
    for student, status in form_data.items():      
        # Insert the attendance data into the database for the student
        insert_attendance(faculty_id, student, course, section, lecture_date, status)
    

    # Confirmation + back
    clear()
    put_text(f"✅ Attendance on {lecture_date} updated for {course} (Sec {section})")
    
    # Buttons for navigation
    put_buttons(
        ['🔙 Back to Attendance', '🏠 Back to Dashboard'],
        onclick=[lambda: mark_attendance(back_to_dashboard, faculty_id), 
                 lambda: back_to_dashboard(faculty_id)]
    )

def mark_attendance(back_to_dashboard, faculty_id):
    # Dashboard listing course×section for attendance marking.
    clear()
    put_markdown('# ✅ Mark Attendance')

    faculty_courses = get_faculty_courses_and_sections(faculty_id)

    rows = []
    for course, secs in faculty_courses.items():
        for sec in secs:
            rows.append([
                course,
                sec,
                put_buttons(
                  ['Mark'],
                  onclick=[lambda c=course, s=sec: handle_mark_attendance(c, s, back_to_dashboard, faculty_id)]
                )
            ])
    put_table([['Course', 'Section', 'Action'], *rows])
