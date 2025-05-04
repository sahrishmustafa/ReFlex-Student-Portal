import sqlite3

def create_course_table(conn):
    # Create the table.
    conn.execute('''
    CREATE TABLE Course (
        courseid TEXT PRIMARY KEY,
        title TEXT,
        credithours INTEGER,
        description TEXT, 
        semester INTEGER
    )
    ''')

    courses = [
        ('CS101', 'Intro to CS', 3, 'Basics of Computer Science', 1),
        ('MATH201', 'Calculus', 4, 'Differential and Integral Calculus', 1)
    ]
    
    conn.executemany('INSERT INTO Course VALUES (?, ?, ?, ?, ?)', courses)

def create_faculty_course_table(conn):
    conn.execute('''
    CREATE TABLE Faculty_Course (
        facultyid INTEGER,
        courseid TEXT,
        sectionid TEXT,
        PRIMARY KEY (facultyid, courseid, sectionid),
        FOREIGN KEY (facultyid) REFERENCES Faculty(id),
        FOREIGN KEY (courseid) REFERENCES Course(courseid)
    )
    ''')

    faculty_course = [
        (1, 'CS101', 'B'),
        (2, 'CS101', 'A')
    ]
    conn.executemany('INSERT INTO Faculty_Course VALUES (?, ?, ?)', faculty_course)

def create_student_course_table(conn):
    conn.execute('''
    CREATE TABLE Student_Course (
        studentid TEXT,
        courseid TEXT,
        sectionid TEXT,
        PRIMARY KEY (studentid, courseid, sectionid),
        FOREIGN KEY (studentid) REFERENCES Student(id),
        FOREIGN KEY (courseid) REFERENCES Course(courseid)
    )
    ''')

    student_course = [
        ('22i-0977', 'CS101', 'A'),
        ('22i-1113', 'CS101', 'A'),
        ('22i-1033', 'CS101', 'A'),
        ('22i-0977', 'MATH201', 'B'),
        ('22i-1113', 'MATH201', 'B')
    ]
    conn.executemany('INSERT INTO Student_Course VALUES (?, ?, ?)', student_course)