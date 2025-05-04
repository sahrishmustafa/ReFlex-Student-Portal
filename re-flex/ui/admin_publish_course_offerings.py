from pywebio.input  import textarea
from pywebio.output import put_markdown, put_text, put_table, put_buttons, clear
from datetime       import datetime

# Terms and in-memory offerings storage
TERMS = ['Spring 2025', 'Fall 2025']
OFFERINGS = {}


def handle_publish_offerings(term, back_to_dashboard, user_email):
    """Prompt for course offerings for a term, tag with email, confirm."""
    clear()
    put_markdown(f"### 📢 Publish Course Offerings: {term} (by {user_email})")
    details   = textarea('Enter courses (e.g., CS101; MATH201; ENG305)', rows=3)
    timestamp = datetime.now().isoformat()
    OFFERINGS[term] = {
        'details': details,
        'published_by': user_email,
        'published_at': timestamp
    }

    clear()
    put_text(f"✅ Offerings for {term} published by {user_email} at {timestamp}.")
    put_buttons(
        ['🔙 Back to Offerings', '🏠 Back to Dashboard'],
        onclick=[
            lambda: publish_course_offerings(back_to_dashboard, user_email),
            back_to_dashboard
        ]
    )


def publish_course_offerings(back_to_dashboard, user_email):
    """Dashboard listing terms with publish actions."""
    clear()
    put_markdown('# 🎓 Publish Course Offerings')
    rows = []
    for term in TERMS:
        entry = OFFERINGS.get(term, {})
        details = entry.get('details', 'None')
        by      = entry.get('published_by', '—')
        at      = entry.get('published_at', '—')
        rows.append([
            term,
            details,
            f"By: {by}\nAt: {at}",
            put_buttons(['Publish'], onclick=[
                lambda t=term: handle_publish_offerings(t, back_to_dashboard, user_email)
            ])
        ])
    put_table([['Term', 'Courses', 'Info', 'Action'], *rows])
