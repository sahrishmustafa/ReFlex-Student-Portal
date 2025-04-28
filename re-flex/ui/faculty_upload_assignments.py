from pywebio.input import select, input, textarea, file_upload
from pywebio.output import put_markdown, put_text, put_buttons, put_table, clear
from datetime import date
from ui.faculty_ui    import faculty_dashboard

# Dummy data for courses and sections
dummy_faculty_courses = {
    'CS101 - Intro to Programming': ['A', 'B'],
    'MATH201 - Calculus II': ['A'],
    'ENG305 - Technical Writing': ['A', 'C']
}

# In-memory store for assignments
ASSIGNMENTS = {}


def handle_upload_assignment(course, section):
    """Upload a single assignment for given course and section."""
    put_markdown(f"### 📤 Upload Assignment for {course} (Section {section})")
    title       = input('Assignment Title')
    description = textarea('Description', rows=3)
    due_date    = input('Due Date (YYYY-MM-DD)', value=str(date.today()))
    attachment  = file_upload('Upload Attachment (PDF, ZIP)', accept='.pdf,.zip')

    # Save dummy
    ASSIGNMENTS.setdefault(course, {}) \
               .setdefault(section, []) \
               .append({
        'title': title,
        'description': description,
        'due_date': due_date,
        'file': attachment['filename']
    })

    # Confirmation screen
    clear()
    put_text(f"✅ Assignment '{title}' uploaded for {course} (Sec {section})")
    put_buttons(
      ['🔙 Back to Assignments', '🏠 Back to Dashboard'],
      onclick=[lambda: upload_assignments(),
               lambda: faculty_dashboard()]
    )


def upload_assignments():
    """Dashboard listing courses × sections for assignment upload."""
    clear()
    put_markdown('# 📚 Upload Assignments')
    rows = []
    for course, sections in dummy_faculty_courses.items():
        for section in sections:
            rows.append([
                course,
                section,
                put_buttons(
                    ['Upload'],
                    onclick=[lambda c=course, s=section: handle_upload_assignment(c, s)]
                )
            ])
    put_table([['Course', 'Section', 'Action'], *rows])

# To integrate, import and call upload_assignments() from your faculty UI dispatcher.
