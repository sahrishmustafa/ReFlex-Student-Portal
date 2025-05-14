from pywebio.input  import input
from pywebio.output import put_markdown, put_text, put_table, put_buttons, clear
from datetime       import datetime

# Dummy semesters
SEMESTERS = ['Spring 2025', 'Fall 2025']

# In-memory timetable store
# Structure: { semester: { 'schedule': str, 'set_by': email, 'set_at': timestamp } }
timetables = {}


def handle_manage_timetable(semester, back_to_dashboard, user_email):
    """Create or update timetable for a semester, then confirm."""
    clear()
    put_markdown(f"### 🗓 Manage Timetable: {semester} (by {user_email})")
    schedule = input('Enter schedule (e.g., CS101 Mon 9-11; MATH201 Tue 10-12)')
    timestamp = datetime.now().isoformat()
    timetables[semester] = {
        'schedule': schedule,
        'set_by': user_email,
        'set_at': timestamp
    }

    clear()
    put_text(f"✅ Timetable for {semester} set by {user_email} at {timestamp}.")
    put_buttons(
        ['🔙 Back to Timetables', '🏠 Back to Dashboard'],
        onclick=[
            lambda: manage_timetables(back_to_dashboard, user_email),
            back_to_dashboard
        ]
    )


def manage_timetables(back_to_dashboard, user_email):
    """Dashboard listing semesters for timetable management."""
    clear()
    put_markdown('# 📋 Manage Timetables')
    rows = []
    for sem in SEMESTERS:
        entry = timetables.get(sem, {})
        sched = entry.get('schedule', 'Not set')
        by    = entry.get('set_by', '—')
        at    = entry.get('set_at', '—')
        rows.append([
            sem,
            sched,
            f"By: {by}\nAt: {at}",
            put_buttons(['Edit'], onclick=[lambda s=sem: handle_manage_timetable(s, back_to_dashboard, user_email)])
        ])
    put_table([['Semester', 'Schedule', 'Info', 'Action'], *rows])
