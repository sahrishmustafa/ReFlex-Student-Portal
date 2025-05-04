from pywebio.input    import input, select
from pywebio.output   import put_markdown, put_text, put_table, put_buttons, clear
from datetime         import datetime

# Dummy requests
REQUESTS = [
    {'id': 1, 'type': 'Course Change',     'detail': 'Switch CS101 to MATH201'},
    {'id': 2, 'type': 'Exam Reschedule',   'detail': 'Move ENG305 final to 2025-06-01'}
]
# In-memory responses
RESPONSES = {}


def handle_request(req, back_to_dashboard, user_email):
    """Process a single request, tag with email, then confirm."""
    clear()
    put_markdown(f"### 🔄 Handle Request #{req['id']} (by {user_email})")
    action = select('Action', ['Approve', 'Deny'])
    note   = input('Optional Note')
    timestamp = datetime.now().isoformat()
    RESPONSES[req['id']] = {
        'action': action,
        'note': note,
        'handled_by': user_email,
        'handled_at': timestamp
    }
    REQUESTS.remove(req)

    clear()
    put_text(f"✅ Request {req['id']} {action}d by {user_email} at {timestamp}.")
    put_buttons([
        '🔙 Back to Requests', '🏠 Back to Dashboard'
    ], onclick=[
        lambda: handle_requests(back_to_dashboard, user_email),
        back_to_dashboard
    ])


def handle_requests(back_to_dashboard, user_email):
    """Dashboard listing all pending requests with Process action."""
    clear()
    put_markdown('# 🛠 Handle Student & Teacher Requests')
    if not REQUESTS:
        put_text('No pending requests!')
        return

    rows = []
    for req in REQUESTS:
        rows.append([
            req['id'],
            req['type'],
            req['detail'],
            put_buttons(['Process'], onclick=[
                lambda r=req: handle_request(r, back_to_dashboard, user_email)
            ])
        ])

    put_table([['ID', 'Type', 'Detail', 'Action'], *rows])
