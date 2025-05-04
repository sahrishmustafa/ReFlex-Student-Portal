# ui/faculty_answer_queries.py

from pywebio.input    import textarea
from pywebio.output   import put_markdown, put_text, put_table, put_buttons, clear

# Dummy pending queries with section context
STUDENT_QUERIES = [
    {'email': 'alice@example.com',   'course': 'CS101 - Intro to Programming', 'section': 'A', 'student': 'Alice',   'query': 'When is the next assignment due?'},
    {'email': 'bob@example.com',     'course': 'MATH201 - Calculus II',       'section': 'A', 'student': 'Bob',     'query': 'Can I get an extension on my quiz?'},
    {'email': 'charlie@example.com', 'course': 'ENG305 - Technical Writing',  'section': 'C', 'student': 'Charlie', 'query': 'Where can I find extra readings?'},
]

# In-memory responses
RESPONSES = []

def handle_respond_query(q, back_to_dashboard, user_email):
    """Prompt a response to a single query, then show confirmation."""
    put_markdown(f"### 💬 Respond to {q['student']} ({q['email']}) @ {q['course']} Sec {q['section']}")
    answer = textarea('Your Response', rows=4)

    # Save dummy with email tag
    RESPONSES.append({
        'query_email': q['email'],
        'response': answer,
        'responded_by': user_email
    })
    STUDENT_QUERIES.remove(q)

    # Confirmation + back buttons
    clear()
    put_text(f"✅ {user_email} sent response to {q['student']} ({q['email']}).")
    put_buttons([
        '🔙 Back to Queries',
        '🏠 Back to Dashboard'
    ], onclick=[
        lambda: respond_student_queries(back_to_dashboard, user_email),
        back_to_dashboard
    ])

def respond_student_queries(back_to_dashboard, user_email):
    """Dashboard showing all pending student queries with Reply actions."""
    clear()
    put_markdown('# 📩 Respond to Student Queries')
    if not STUDENT_QUERIES:
        put_text('No pending queries!')
        return

    rows = []
    for q in STUDENT_QUERIES:
        rows.append([
            q['email'],
            q['course'],
            q['section'],
            q['student'],
            q['query'],
            put_buttons([
                'Reply'
            ], onclick=[
                lambda qq=q: handle_respond_query(qq, back_to_dashboard, user_email)
            ])
        ])

    put_table([['Email', 'Course', 'Section', 'Student', 'Query', 'Action'], *rows])
