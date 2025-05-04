# ui/faculty_upload_assignments.py

from datetime         import date
from pywebio.input    import select, input, textarea, file_upload
from pywebio.output   import put_markdown, put_text, put_buttons, put_table, clear

from database.course_db import get_faculty_courses_and_sections
from database.assignment_db import insert_assignment

def handle_upload_assignment(course, section, back_to_dashboard, faculty_id):
    # Upload a single assignment for given course and section, then show confirmation.
    put_markdown(f"### 📤 Upload Assignment for {course} (Sec {section}) by {faculty_id}")

    title       = input('Assignment Title')
    description = textarea('Description', rows=3)
    due_date    = input("Enter the lecture date", type="date")
    attachment  = file_upload('Upload Attachment (PDF, ZIP)', accept='.pdf')

    # Save data to the assignment
    insert_assignment(faculty_id, course, section, title, description, due_date, attachment)

    # Confirmation screen
    clear()
    put_text(f"✅ {faculty_id} uploaded assignment '{title}' for {course} (Sec {section})")
    put_buttons([
        '🔙 Back to Assignments',
        '🏠 Back to Dashboard'
    ], onclick=[
        lambda: upload_assignments(back_to_dashboard, faculty_id),
        back_to_dashboard
    ])


def upload_assignments(back_to_dashboard, faculty_id):
    """Dashboard listing courses × sections for assignment upload."""
    clear()
    put_markdown('# 📚 Upload Assignments')

    faculty_courses = get_faculty_courses_and_sections(faculty_id)
    
    rows = []
    for course, sections in faculty_courses.items():
        for section in sections:
            rows.append([
                course,
                section,
                put_buttons([
                    'Upload'
                ], onclick=[
                    lambda c=course, s=section: handle_upload_assignment(c, s, back_to_dashboard, faculty_id)
                ])
            ])
    put_table([['Course', 'Section', 'Action'], *rows])
