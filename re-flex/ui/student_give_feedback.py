from pywebio.input import textarea
from pywebio.output import put_markdown, put_buttons, toast, clear

from database.requests_db import insert_request

def give_feedback(user_email, go_back_callback):
    clear()
    put_markdown("## 💬 Give Feedback")

    feedback_text = textarea("Your Feedback", placeholder="Write your comments or suggestions here...", rows=5)
    
    if feedback_text.strip():  
        insert_request(user_email, 'Teacher Feedback', feedback_text)
        toast("✅ Feedback submitted. Thank you!")
    else:
        toast("⚠️ Please enter some feedback before submitting.")

    put_buttons(['Back to Dashboard'], onclick=[lambda: go_back_callback(user_email)])
