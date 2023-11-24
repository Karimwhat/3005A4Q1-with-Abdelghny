# 3005A4Q1-with-Abdelghny

Karim Fouad - 101244311

Link: https://youtu.be/UN4pvQn7Byg


# Students Database Application


This Python application interfaces with a PostgreSQL database to perform CRUD operations on a 'students' table.

// Setup Instructions for the Database

1. Install PostgreSQL/pgAdmin4.
2. Create a new database named `studentsA4` or change it in the code and match your new name with it.
3. Using pgAdmin4's Query Tool, create the `students` table with columns according to the assignment instructions:
4. Insert initial data into the `students` table using the provided SQL script in the assignment instructions.

// Steps to Compile and Run the Application

1. Install Python
2. Install the `psycopg2` library using the command: `pip install psycopg2`.
3. Run the application with the command: `python Application.py`.

// Function Descriptions

- `connect_to_database()`: Creates a connection to the PostgreSQL database using provided credentials.
- `getAllStudents()`: Retrieves and prints all records from the `students` table.
- `addStudent(first_name, last_name, email, enrollment_date)`: Inserts a new student record into the `students` table.
- `updateStudentEmail(student_id, new_email)`: Updates the email address for a student with the specified `student_id`.
- `deleteStudent(student_id)`: Deletes the record of the student with the specified `student_id`.

