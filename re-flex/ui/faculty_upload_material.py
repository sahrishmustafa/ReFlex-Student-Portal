from pywebio.input    import file_upload
from pywebio.output   import put_markdown, put_text, put_table, put_buttons, clear

# Dummy data for courses and sections
dummy_faculty_courses = {
    'CS101 - Intro to Programming': ['A', 'B'],
    'MATH201 - Calculus II':             ['A'],
    'ENG305 - Technical Writing':        ['A', 'C'],
}

# In-memory store for uploaded materials
COURSE_MATERIALS = {}


def handle_upload_course_material(course, section, back_to_dashboard):
    """Handle file upload and show confirmation."""
    put_markdown(f"### 📂 Upload Materials for {course} (Sec {section})")
    materials = file_upload(
        'Select Files (PDF, PPTX, DOCX)',
        accept='.pdf,.pptx,.docx',
        multiple=True
    )

    COURSE_MATERIALS.setdefault(course, {}) \
                    .setdefault(section, []) \
                    .extend([m['filename'] for m in materials])

    # Confirmation screen
    clear()
    put_text(f"✅ Materials for {course} (Sec {section}) Uploaded Successfully!")
    put_buttons(
        ['🔙 Back to Materials', '🏠 Back to Dashboard'],
        onclick=[
            lambda: upload_course_materials(back_to_dashboard),
            back_to_dashboard
        ]
    )


def upload_course_materials(back_to_dashboard):
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
                    onclick=[lambda c=course, s=sec: handle_upload_course_material(c, s, back_to_dashboard)]
                )
            ])
    put_table([['Course', 'Section', 'Action'], *rows])
