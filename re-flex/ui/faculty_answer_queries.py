from pywebio.input    import input, textarea
from pywebio.output   import put_markdown, put_text, put_table, put_buttons, clear

# Dummy pending queries with section context
STUDENT_QUERIES = [
    {'id': 1, 'course': 'CS101 - Intro to Programming', 'section': 'A', 'student': 'Alice',   'query': 'When is the next assignment due?'},
    {'id': 2, 'course': 'MATH201 - Calculus II',       'section': 'A', 'student': 'Bob',     'query': 'Can I get an extension on my quiz?'},
    {'id': 3, 'course': 'ENG305 - Technical Writing',  'section': 'C', 'student': 'Charlie', 'query': 'Where can I find extra readings?'},
]

# In-memory responses
RESPONSES = []


def handle_respond_query(q, back_to_dashboard):
    """Prompt a response to a single query, then show confirmation."""
    put_markdown(f"### 💬 Respond to {q['student']} (@ {q['course']} Sec {q['section']})")
    answer = textarea('Your Response', rows=4)

    # Save dummy
    RESPONSES.append({'query_id': q['id'], 'response': answer})
    STUDENT_QUERIES.remove(q)

    # Confirmation + back buttons
    clear()
    put_text(f"✅ Your response to Query #{q['id']} has been sent.")
    put_buttons([
        '🔙 Back to Queries',
        '🏠 Back to Dashboard'
    ], onclick=[
        lambda: respond_student_queries(back_to_dashboard),
        back_to_dashboard
    ])


def respond_student_queries(back_to_dashboard):
    """Dashboard showing all pending student queries with Reply actions."""
    clear()
    put_markdown('# 📩 Respond to Student Queries')
    if not STUDENT_QUERIES:
        put_text('No pending queries!')
        return

    rows = []
    for q in STUDENT_QUERIES:
        rows.append([
            q['id'], q['course'], q['section'], q['student'], q['query'],
            put_buttons([
                'Reply'
            ], onclick=[
                lambda qq=q: handle_respond_query(qq, back_to_dashboard)
            ])
        ])

    put_table([['ID', 'Course', 'Section', 'Student', 'Query', 'Action'], *rows])
