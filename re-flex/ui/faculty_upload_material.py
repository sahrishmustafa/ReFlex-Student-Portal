# ui/faculty_upload_materials.py

from pywebio.input    import file_upload
from pywebio.output   import put_markdown, put_text, put_table, put_buttons, clear
from datetime         import datetime

# Dummy data for courses and sections
dummy_faculty_courses = {
    'CS101 - Intro to Programming': ['A', 'B'],
    'MATH201 - Calculus II':             ['A'],
    'ENG305 - Technical Writing':        ['A', 'C'],
}

# In-memory store for uploaded materials
COURSE_MATERIALS = {}


def handle_upload_course_material(course, section, back_to_dashboard, user_email):
    """Handle file upload and show confirmation."""
    put_markdown(f"### 📂 Upload Materials for {course} (Sec {section}) by {user_email}")
    materials = file_upload(
        'Select Files (PDF, PPTX, DOCX)',
        accept='.pdf,.pptx,.docx',
        multiple=True
    )

    timestamp = datetime.now().isoformat()
    entries = [{
        'file': m['filename'],
        'uploaded_by': user_email,
        'uploaded_at': timestamp
    } for m in materials]

    COURSE_MATERIALS.setdefault(course, {}) \
                    .setdefault(section, []) \
                    .extend(entries)

    # Confirmation screen
    clear()
    put_text(f"✅ {len(entries)} file(s) uploaded for {course} (Sec {section}) by {user_email}")
    put_buttons(
        ['🔙 Back to Materials', '🏠 Back to Dashboard'],
        onclick=[
            lambda: upload_course_materials(back_to_dashboard, user_email),
            back_to_dashboard
        ]
    )


def upload_course_materials(back_to_dashboard, user_email):
    """Display dashboard of courses × sections with upload actions."""
    clear()
    put_markdown('# 📚 Upload Course Materials')
    rows = []
    for course, secs in dummy_faculty_courses.items():
        for sec in secs:
            rows.append([
                course,
                sec,
                put_buttons(
                    ['Upload'],
                    onclick=[lambda c=course, s=sec: handle_upload_course_material(c, s, back_to_dashboard, user_email)]
                )
            ])
    put_table([['Course', 'Section', 'Action'], *rows])
