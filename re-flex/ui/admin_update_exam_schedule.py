from pywebio.input  import input
from pywebio.output import put_markdown, put_text, put_table, put_buttons, clear
from datetime       import datetime

# Dummy sessions
EXAM_SESSIONS = ['Midterm', 'Final']

# In-memory exam schedule
# Structure: { session: { 'details': str, 'set_by': email, 'set_at': timestamp } }
EXAM_SCHEDULE = {}

def handle_update_exam(session, back_to_dashboard, user_email):
    """Update schedule for a session, then confirm."""
    clear()
    put_markdown(f"### 📝 Update Exam Schedule: {session} (by {user_email})")
    details   = input('Enter details (e.g., CS101 2025-05-10 10:00 Room 101)')
    timestamp = datetime.now().isoformat()
    EXAM_SCHEDULE[session] = {
        'details': details,
        'set_by': user_email,
        'set_at': timestamp
    }

    clear()
    put_text(f"✅ {session} schedule set by {user_email} at {timestamp}.")
    put_buttons(
        ['🔙 Back to Exam Schedules', '🏠 Back to Dashboard'],
        onclick=[
            lambda: update_exam_schedule(back_to_dashboard, user_email),
            back_to_dashboard
        ]
    )

def update_exam_schedule(back_to_dashboard, user_email):
    """Dashboard listing exam sessions for schedule updates."""
    clear()
    put_markdown('# 📅 Update Exam Schedules')
    rows = []
    for sess in EXAM_SESSIONS:
        entry = EXAM_SCHEDULE.get(sess, {})
        details = entry.get('details', 'Not set')
        by      = entry.get('set_by', '—')
        at      = entry.get('set_at', '—')
        rows.append([
            sess,
            f"{details}",
            f"By: {by}\nAt: {at}",
            put_buttons(['Edit'], onclick=[
                lambda s=sess: handle_update_exam(s, back_to_dashboard, user_email)
            ])
        ])
    put_table([['Session','Details','Info','Action'], *rows])
