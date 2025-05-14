from pywebio.input    import input, textarea
from pywebio.output   import put_markdown, put_text, put_table, put_buttons, clear

from database.studentquery_db import get_student_queries_for_faculty
from database.studentquery_db import update_student_query_answer

def handle_respond_query(q, back_to_dashboard, STUDENT_QUERIES, faculty_id):
    # Prompt a response to a single query, then show confirmation.
    put_markdown(f"### Respond to {q['student']} (@ {q['course']} Sec {q['section']})")
    answer = textarea('Your Response', rows=4)

    # Give response to the student. 
    update_student_query_answer(q['id'], answer)

    # Confirmation + back buttons
    clear()
    put_text(f"Your response to Query #{q['id']} has been sent.")
    put_buttons([
        '🔙 Back to Queries',
        '🏠 Back to Dashboard'
    ], onclick=[
        lambda: respond_student_queries(back_to_dashboard, faculty_id),
        back_to_dashboard(faculty_id)
    ])


def respond_student_queries(back_to_dashboard, faculty_id):
    # Dashboard showing all pending student queries with Reply actions.
    clear()
    put_markdown('# 📩 Respond to Student Queries')
    
    # Pending queries with section context
    STUDENT_QUERIES = get_student_queries_for_faculty(faculty_id)
    
    if not STUDENT_QUERIES:
        put_text('No pending queries!')
        
        put_buttons(
            ['Back to Dashboard'],
            onclick=[lambda: back_to_dashboard(faculty_id)]
        )

    rows = []
    for q in STUDENT_QUERIES:
        rows.append([
            q['id'], q['course'], q['section'], q['student'], q['query'],
            put_buttons([
                'Reply'
            ], onclick=[
                lambda qq=q: handle_respond_query(qq, back_to_dashboard, STUDENT_QUERIES, faculty_id)
            ])
        ])

    if STUDENT_QUERIES: put_table([['ID', 'Course', 'Section', 'Student', 'Query', 'Action'], *rows])
