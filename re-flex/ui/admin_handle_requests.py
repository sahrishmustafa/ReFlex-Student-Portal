from datetime         import datetime
from pywebio.input    import input, select
from pywebio.output   import put_markdown, put_text, put_table, put_buttons, clear

from database.requests_db import get_students_request
from database.requests_db import update_request

def handle_request(req, back_to_dashboard, user_email):
    # Process a single request, tag with email, then confirm.
    clear()
    put_markdown(f"### 🔄 Handle Request #{req['id']} (by {user_email})")
    
    action = select('Action', ['Approve', 'Deny'])
    note   = input('Optional Note')

    # Update the request. 
    update_request(req['id'], action, note)

    clear()
    put_text(f"✅ Request {req['id']} {action}d by {user_email}.")
    put_buttons([
        '🔙 Back to Requests', '🏠 Back to Dashboard'
    ], onclick=[
        lambda: handle_requests(back_to_dashboard, user_email),
        back_to_dashboard
    ])


def handle_requests(back_to_dashboard, user_email):
    # Dashboard listing all pending requests with Process action.
    clear()
    put_markdown('# 🛠 Handle Student Requests')

    REQUESTS = get_students_request()
    
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
