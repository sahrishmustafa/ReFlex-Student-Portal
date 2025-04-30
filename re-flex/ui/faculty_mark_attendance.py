from pywebio.input    import checkbox
from pywebio.output   import put_markdown, put_text, put_buttons, put_table, clear
from datetime         import date

# Dummy course→sections mapping
dummy_faculty_courses = {
    'CS101 - Intro to Programming': ['A', 'B'],
    'MATH201 - Calculus II':             ['A'],
    'ENG305 - Technical Writing':        ['A', 'C'],
}

# Dummy students list (same for all sections here)
STUDENTS = ['Alice Johnson', 'Bob Smith', 'Charlie Lee']

# In-memory attendance store
ATTENDANCE = {}


def handle_mark_attendance(course, section, back_to_dashboard):
    """Mark present/absent for one lecture, then show confirmation."""
    put_markdown(f"### 🗓️ Mark Attendance for {course} (Sec {section})")
    lecture_date = date.today().isoformat()
    present      = checkbox('Select Present Students', STUDENTS)

    # Save dummy
    ATTENDANCE.setdefault(course, {}) \
              .setdefault(section, {})[lecture_date] = present

    # Compute absent
    absent = [s for s in STUDENTS if s not in present]

    # Confirmation + back
    clear()
    put_text(f"✅ Attendance on {lecture_date} updated for {course} (Sec {section})")
    put_text(f"• Present: {', '.join(present) or '—'}")
    put_text(f"• Absent:  {', '.join(absent)  or '—'}")
    put_buttons(
        ['🔙 Back to Attendance', '🏠 Back to Dashboard'],
        onclick=[
            lambda: mark_attendance(back_to_dashboard),
            back_to_dashboard
        ]
    )


def mark_attendance(back_to_dashboard):
    """Dashboard listing course×section for attendance marking."""
    clear()
    put_markdown('# ✅ Mark Attendance')
    rows = []
    for course, secs in dummy_faculty_courses.items():
        for sec in secs:
            rows.append([
                course,
                sec,
                put_buttons(
                  ['Mark'],
                  onclick=[lambda c=course, s=sec: handle_mark_attendance(c, s, back_to_dashboard)]
                )
            ])
    put_table([['Course', 'Section', 'Action'], *rows])
