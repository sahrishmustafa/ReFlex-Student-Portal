from pywebio.input import textarea
from pywebio.output import put_markdown, put_buttons, toast, clear
from database.student_db import submit_feedback  # Dummy function to store feedback

def give_feedback(user_email, go_back_callback):
    clear()
    put_markdown("## 💬 Give Feedback")

    feedback_text = textarea("Your Feedback", placeholder="Write your comments or suggestions here...", rows=5)

    if feedback_text:
        submit_feedback(user_email, feedback_text)
        toast("✅ Feedback submitted. Thank you!")

    put_buttons(['Back to Dashboard'], onclick=[lambda: go_back_callback(user_email)])
