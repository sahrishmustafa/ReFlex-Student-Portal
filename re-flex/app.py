import os
import sqlite3

from pywebio import start_server
from pywebio.input import input, input_group
from pywebio.output import put_text, put_error, put_success, clear

from models.__init__ import init_db

from ui.faculty_ui import faculty_dashboard

if not os.path.exists('reflex.db'):
    init_db()

# Note: Placeholders, will be replaced later on.
def student_dashboard(email):
    put_text(f"Welcome, {email}! This is your Student Dashboard.")

def admin_dashboard(email):
    put_text(f"Welcome, {email}! This is your Admin Dashboard.")

def login():
    user_input = input_group("Login", [
        input("Email", name='email', type='text', required=True),
        input("Password", name='password', type='password', required=True)
    ])

    email = user_input['email']
    password = user_input['password']

    conn = sqlite3.connect('reflex.db')
    cursor = conn.cursor()
    cursor.execute("SELECT password, role FROM RegisteredUsers WHERE email = ?", (email,))
    result = cursor.fetchone()
    conn.close()

    if result:
        db_password, role = result
        if password == db_password:
            clear()
            put_success(f"Login successful")
            if role == 'Faculty':
                faculty_dashboard(email)
            elif role == 'Student':
                student_dashboard(email)
            elif role == 'Admin':
                admin_dashboard(email)
            else:
                put_error("Unknown role.")
        else:
            put_error("Incorrect password.")
    else:
        put_error("User not found.")

# def main():
#     faculty_dashboard("imran.ashraf@gmail.com")

if __name__ == "__main__":
    start_server(login, port=8080)
