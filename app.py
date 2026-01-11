import sqlite3
from db import connect_db

def add_student():
    name = input("Enter name: ")
    age = input("Enter age: ")
    course = input("Enter course: ")

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO students (name, age, course) VALUES (?, ?, ?)",
        (name, age, course)
    )

    conn.commit()
    conn.close()
    print("Student added successfully\n")

def view_students():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()

    print("\nID | Name | Age | Course")
    print("-" * 30)
    for row in rows:
        print(row)

    conn.close()

while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice")
