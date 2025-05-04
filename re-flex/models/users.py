import sqlite3

def create_registered_users(conn):
    # Create the table
    conn.execute('''
    CREATE TABLE RegisteredUsers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL,
        role TEXT NOT NULL CHECK (role IN ('Student', 'Faculty', 'Admin'))
    );
    ''')

    # Insert all users
    conn.executescript('''
    -- Insert Students
    INSERT INTO RegisteredUsers (email, password, role) VALUES 
    ('i220977@gmail.com', 'sahrish', 'Student'),
    ('i221033@gmail.com', 'maria', 'Student'),
    ('i221113@gmail.com', 'hadiya', 'Student'),
    ('student4@example.com', 'hashed_password_4', 'Student'),
    ('student5@example.com', 'hashed_password_5', 'Student');

    -- Insert Faculty
    INSERT INTO RegisteredUsers (email, password, role) VALUES 
    ('javaria.zia@gmail.com', 'javaria', 'Faculty'),
    ('imran.ashraf@gmail.com', 'imran', 'Faculty'),
    ('hammad.majeed@gmail.com', 'hammad', 'Faculty'),
    ('faculty4@example.com', 'hashed_password_9', 'Faculty'),
    ('faculty5@example.com', 'hashed_password_10', 'Faculty');

    -- Insert Admins
    INSERT INTO RegisteredUsers (email, password, role) VALUES 
    ('admin1@example.com', 'hashed_password_11', 'Admin'),
    ('admin2@example.com', 'hashed_password_12', 'Admin'),
    ('admin3@example.com', 'hashed_password_13', 'Admin'),
    ('admin4@example.com', 'hashed_password_14', 'Admin'),
    ('admin5@example.com', 'hashed_password_15', 'Admin');
    ''')

