import pyodbc

conn = pyodbc.connect(
'DRIVER={ODBC Driver 17 for SQL Server};'
'SERVER=localhost;'
'DATABASE=StudentDB;'
'Trusted_Connection=yes;'
)

cursor = conn.cursor()

# Add student
def add_student():
    name = input("Enter name: ")
    age = input("Enter age: ")
    Department = input("Enter Department: ")
    College = input("Enter College: ")
    course = input("Enter course: ")

    cursor.execute(
    "INSERT INTO Students(Name,Age,Department,College,Course) VALUES(?,?,?)",
    (name,age,course)
    )
    conn.commit()
    print("Student added successfully")

# View students
def view_students():
    cursor.execute("SELECT * FROM Students")
    rows = cursor.fetchall()

    for row in rows:
        print(row)

# Update student
def update_student():
    sid = input("Enter Student ID to update: ")
    name = input("Enter new name: ")

    cursor.execute(
    "UPDATE Students SET Name=? WHERE StudentID=?",
    (name,sid)
    )
    conn.commit()
    print("Student updated")

# Delete student
def delete_student():
    sid = input("Enter Student ID to delete: ")

    cursor.execute(
    "DELETE FROM Students WHERE StudentID=?",
    (sid)
    )
    conn.commit()
    print("Student deleted")

# Menu
while True:

    print("\nStudent Management System")
    print("1 Add Student")
    print("2 View Students")
    print("3 Update Student")
    print("4 Delete Student")
    print("5 Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        add_student()

    elif choice == 2:
        view_students()

    elif choice == 3:
        update_student()

    elif choice == 4:
        delete_student()

    elif choice == 5:
        break