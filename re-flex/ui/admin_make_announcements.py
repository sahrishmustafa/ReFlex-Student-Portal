import os
import sqlite3
import yagmail  # Replaced smtplib with yagmail
from pywebio.input import textarea, input, file_upload, input_group, TEXT
from pywebio.output import put_markdown, put_text, put_table, put_buttons, clear

os.environ["EMAIL_PASSWORD"] = "your password"

def get_students_emails(semester):
    # Convert semester to string if it's a number
    semester = str(semester).strip()  # Ensure it's a string
    
    conn = sqlite3.connect('reflex.db')
    cursor = conn.cursor()

    if semester.lower() == 'all':
        cursor.execute("SELECT email FROM Student")
    else:
        cursor.execute("SELECT email FROM Student WHERE semester = ?", (int(semester),))
    
    rows = cursor.fetchall()
    conn.close()

    return [row[0] for row in rows]

def send_email(user_email, subject, message, students_emails, attachment=None):
    sender_email = str(user_email).strip()
    sender_password = os.getenv('EMAIL_PASSWORD')

    if not sender_password:
        print("EMAIL_PASSWORD not set.")
        return False

    try:
        # Initialize yagmail SMTP connection
        yag = yagmail.SMTP(sender_email, sender_password)

        for student_email in students_emails:
            student_email = str(student_email).strip()
            
            # Prepare attachments if exists
            attachments = [attachment] if attachment else None
            
            # Send email using yagmail
            yag.send(
                to=student_email,
                subject=subject,
                contents=message,
                attachments=attachments
            )
            print(f"Email sent to {student_email}")

        return True

    except Exception as e:
        print(f"Error sending email: {e}")
        return False

def make_announcements(back_to_dashboard, user_email):
    clear()
    put_markdown(f"### 📢 Create a New Announcement (by {user_email})")

    data = input_group("📢 Send Announcement", [
        input('Semester (Number or "All")', name='semester', type=TEXT),
        input('Subject of the Announcement', name='subject'),
        textarea('Announcement Message', rows=5, name='message'),
        file_upload("Attach a file (optional, PDF/Excel)", accept='.pdf,.xlsx', name='file')
    ])

    semester = data['semester'].strip()
    subject = data['subject']
    message = data['message']
    file = data.get('file') 
    
    file_content = file['content'] if file else None

    students_emails = get_students_emails(semester)

    print("Students emails:", students_emails)
    print("Subject:", subject, type(subject))
    print("Message:", message, type(message))

    email_sent = send_email(user_email, subject, message, students_emails, file_content)
    
    if email_sent:
        clear()
        put_text(f"✅ Announcement '{subject}' sent to students.")
    else:
        put_text(f"❌ Failed to send the email. Please check your email settings.")

    put_buttons(
        ['🏠 Back to Dashboard'],
        onclick=[back_to_dashboard]
    )