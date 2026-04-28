import sqlite3

def connect():
    conn = sqlite3.connect("students.db")
    return conn

def create_table():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS students (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, age INTEGER, course TEXT, marks REAL)''')
    conn.commit()
    conn.close()

def add_student():
    name = input("Enter Name: ")
    age = input("Enter Age: ")
    course = input("Enter Course: ")
    marks = input("Enter Marks: ")
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO students (name, age, course, marks) VALUES (?, ?, ?, ?)", (name, age, course, marks))
    conn.commit()
    conn.close()
    print("Student Added!")

def view_students():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    conn.close()
    if rows:
        for row in rows:
            print(f"ID:{row[0]} Name:{row[1]} Age:{row[2]} Course:{row[3]} Marks:{row[4]}")
    else:
        print("No students found!")

def delete_student():
    view_students()
    sid = input("Enter ID to delete: ")
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM students WHERE id=?", (sid,))
    conn.commit()
    conn.close()
    print("Deleted!")

def update_student():
    view_students()
    sid = input("Enter ID to update: ")
    name = input("New Name: ")
    age = input("New Age: ")
    course = input("New Course: ")
    marks = input("New Marks: ")
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("UPDATE students SET name=?, age=?, course=?, marks=? WHERE id=?", (name, age, course, marks, sid))
    conn.commit()
    conn.close()
    print("Updated!")

def main():
    create_table()
    while True:
        print("\n===== Student Record System =====")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Exit")
        choice = input("Enter Choice: ")
        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            update_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")

main()