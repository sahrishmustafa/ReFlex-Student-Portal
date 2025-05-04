from pywebio.input    import textarea
from pywebio.output   import put_markdown, put_text, put_table, put_buttons, clear
from datetime         import datetime

# In-memory announcements store as list of dicts
ANNOUNCEMENTS = []

def handle_make_announcement(back_to_dashboard, user_email):
    """Prompt for announcement content, tag with email and timestamp, then confirm."""
    clear()
    put_markdown('### 📣 Make Announcement')
    content   = textarea('Title and Content', rows=4)
    timestamp = datetime.now().isoformat()
    ANNOUNCEMENTS.append({
        'content': content,
        'posted_by': user_email,
        'posted_at': timestamp
    })

    clear()
    put_text(f"✅ Announcement posted by {user_email} at {timestamp}!")
    put_buttons([
        '🔙 Back to Announcements',
        '🏠 Back to Dashboard'
    ], onclick=[
        lambda: make_announcements(back_to_dashboard, user_email),
        back_to_dashboard
    ])

def make_announcements(back_to_dashboard, user_email):
    """Display list of posted announcements with option to add new."""
    clear()
    put_markdown('# 📢 Send University Announcements')
    if not ANNOUNCEMENTS:
        put_text('No announcements yet!')
    else:
        rows = [
            [i+1,
             a['content'],
             f"By: {a['posted_by']}\nAt: {a['posted_at']}"
            ]
            for i, a in enumerate(ANNOUNCEMENTS)
        ]
        put_table([['#', 'Content', 'Info'], *rows])
    put_buttons(['New'], onclick=[lambda: handle_make_announcement(back_to_dashboard, user_email)])
