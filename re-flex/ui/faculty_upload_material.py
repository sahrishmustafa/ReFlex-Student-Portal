# ui/faculty_upload_materials.py

from datetime         import datetime
from pywebio.input    import select, input, textarea, file_upload
from pywebio.output   import put_markdown, put_text, put_table, put_buttons, clear

from database.course_db import get_faculty_courses_and_sections
from database.material_db import insert_material

def handle_upload_course_material(course, section, back_to_dashboard, faculty_id):
    """Handle file upload and show confirmation."""
    put_markdown(f"### 📂 Upload Materials for {course} (Sec {section}) by {faculty_id}")
    
    title       = input('Assignment Title')
    description = textarea('Description', rows=3)
    materials = file_upload(
        'Select Files (PDF, PPTX, DOCX)',
        accept='.pdf,.pptx,.docx',
        multiple=True
    )

    # Insert the data. 
    insert_material(faculty_id, course, section, title, description, materials)

    # Confirmation screen
    clear()
    put_text(f"✅ {len(entries)} file(s) uploaded for {course} (Sec {section}) by {faculty_id}")
    put_buttons(
        ['🔙 Back to Materials', '🏠 Back to Dashboard'],
        onclick=[
            lambda: upload_course_materials(back_to_dashboard, user_email),
            back_to_dashboard
        ]
    )


def upload_course_materials(back_to_dashboard, faculty_id):
    """Display dashboard of courses × sections with upload actions."""
    clear()
    put_markdown('# 📚 Upload Course Materials')

    faculty_courses = get_faculty_courses_and_sections(faculty_id)

    rows = []
    for course, secs in faculty_courses.items():
        for sec in secs:
            rows.append([
                course,
                sec,
                put_buttons(
                    ['Upload'],
                    onclick=[lambda c=course, s=sec: handle_upload_course_material(c, s, back_to_dashboard, faculty_id)]
                )
            ])
    
    put_table([['Course', 'Section', 'Action'], *rows])
