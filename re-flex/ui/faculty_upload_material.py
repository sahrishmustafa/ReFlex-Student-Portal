from pywebio.input import file_upload
from pywebio.output import put_markdown, put_table, put_text, put_buttons, clear
from ui.faculty_ui    import faculty_dashboard

# Dummy data for courses and sections
dummy_faculty_courses = {
    'CS101 - Intro to Programming': ['A', 'B'],
    'MATH201 - Calculus II': ['A'],
    'ENG305 - Technical Writing': ['A', 'C']
}

# In-memory store for uploaded materials
COURSE_MATERIALS = {}

def upload_course_material(course, section):
    """Handle actual file upload and show confirmation."""
    put_markdown(f"### Upload Materials for {course} (Section {section})")
    materials = file_upload(
        'Select Files (PDF, PPTX, DOCX)',
        accept='.pdf,.pptx,.docx',
        multiple=True
    )

    # Dummy save logic
    COURSE_MATERIALS.setdefault(course, {}).setdefault(section, []).extend(
        [m['filename'] for m in materials]
    )

    # Confirmation screen
    clear()
    put_text(f"✅ Materials for {course} (Section {section}) Uploaded Successfully!")
    put_buttons(
      ['🔙 Back to Course Materials', '🏠 Back to Dashboard'],
      onclick=[lambda: upload_course_materials(),
               lambda: faculty_dashboard()]
    )


def upload_course_materials():
    """Display dashboard of courses × sections with upload actions."""
    clear()
    put_markdown('# Upload Course Materials')
    table_rows = []
    for course, sections in dummy_faculty_courses.items():
        for section in sections:
            table_rows.append([
                course,
                section,
                put_buttons(
                    ['Upload'],
                    onclick=[lambda c=course, s=section: upload_course_material(c, s)]
                )
            ])

    put_table([
        ['Course', 'Section', 'Action'],
        *table_rows
    ])

# To integrate, import and call upload_course_materials() from your main faculty UI dispatcher.
