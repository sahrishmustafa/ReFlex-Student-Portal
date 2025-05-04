from pywebio.input import select, actions
from pywebio.output import put_text, put_buttons, put_markdown, toast, clear
from database.student_db import get_available_courses

def course_registration(user_email, go_back_callback):
    clear()
    put_markdown(f"## 📚 Course Registration for {user_email}")
    
    # Step 1: Get available courses from the DB (dummy function)
    available_courses = get_available_courses(user_email)
    
    if not available_courses:
        put_text("No courses available for registration at the moment.")
        put_buttons(['Back to Dashboard'], onclick=[lambda: go_back_callback(user_email)])
        return
    
    # Step 2: Let user pick a course
    course_id = select("Select a course to register:", options=[
        f"{course['id']} - {course['name']}" for course in available_courses
    ])
    
    # Step 3: Confirm registration
    result = actions("Do you want to register for this course?", buttons=[
        {'label': 'Register', 'value': 'register'},
        {'label': 'Cancel', 'value': 'cancel'}
    ])
    
    if result == 'register':
        # (Dummy) pretend to register 
        ########################################
        #REGISTER HERE @ DB
        ########################################
        toast(f"✅ Successfully registered for {course_id}")
    else:
        toast("❌ Registration canceled")

    # Step 4: Return option
    put_buttons(['Back to Dashboard'], onclick=[lambda: go_back_callback(user_email)])
