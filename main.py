#Step 3: Import and Connect to SQLite
import sqlite3
# Connect to database (creates file automatically)
conn = sqlite3.connect("student.db")
# Create cursor
cursor = conn.cursor()
print("Database connected successfully")

#Step 4: Create Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    course TEXT
)
""")
conn.commit()

#Step 5: Insert Data Function
def add_student():
   name = input("Enter Name: ")
   age = int(input("Enter Age: "))
   course = input("Enter Course: ")
   cursor.execute(
      "INSERT INTO students (name, age, course) VALUES (?, ?, ?)",
      (name, age, course)
   )
   conn.commit()
   print("Student added successfully")

#Step 6: View Data
def view_students():
   cursor.execute("SELECT * FROM students")
   rows = cursor.fetchall()
   print("\n--- Student Records ---")
   for row in rows:
      print(f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}, Course: {row[3]}")

#Step 7: Update Data
def update_student():
   sid = int(input("Enter Student ID: "))
   name = input("Enter New Name: ")
   age = int(input("Enter New Age: "))
   course = input("Enter New Course: ")

   cursor.execute("""
    UPDATE students
    SET name=?, age=?, course=?
    WHERE id=?
    """, (name, age, course, sid))
   conn.commit()
   print("Student updated successfully")

#Step 8: Delete Data
def delete_student():
   sid = int(input("Enter Student ID to delete: "))

   cursor.execute("DELETE FROM students WHERE id=?", (sid,))
   conn.commit()
   print("Student deleted successfully")

#Step 9: Menu-Driven Program (Main Logic)
def menu():
   while True:
      print("\n===== Student Database Menu =====")
      print("1. Add Student")
      print("2. View Students")
      print("3. Update Student")
      print("4. Delete Student")
      print("5. Exit")
      choice = input("Enter your choice: ")
      if choice == '1':
         add_student()
      elif choice == '2':
         view_students()
      elif choice == '3':
         update_student()
      elif choice == '4':
         delete_student()
      elif choice == '5':
         print("Exiting program...")
         break
      else:
         print("Invalid choice")
menu()

#Step 10: Close Connection
conn.close()