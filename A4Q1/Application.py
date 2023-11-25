import psycopg2

# Database connection parameters
DB_HOST = 'localhost'
DB_NAME = 'studentsA4'
DB_USER = 'postgres'
DB_PASS = 'student'  
DB_PORT = '3000'

# Function to connect to the database
def connect_to_database():
    conn = psycopg2.connect(dbname = DB_NAME, user = DB_USER, password = DB_PASS, host = DB_HOST, port = DB_PORT)
    return conn

# Function to get all students
def getAllStudents():
    conn = connect_to_database()
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM students;")
        records = cur.fetchall()
        for record in records:
            print(record)
    conn.close()

# Function to add a student
def addStudent(first_name, last_name, email, enrollment_date):
    conn = connect_to_database()
    with conn.cursor() as cur:
        cur.execute(
            "INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s);",
            (first_name, last_name, email, enrollment_date)
        )
        conn.commit()
    conn.close()

# Function to update a student's email
def updateStudentEmail(student_id, new_email):
    conn = connect_to_database()
    with conn.cursor() as cur:
        cur.execute(
            "UPDATE students SET email = %s WHERE student_id = %s;",
            (new_email, student_id)
        )
        conn.commit()
    conn.close()

# Function to delete a student
def deleteStudent(student_id):
    conn = connect_to_database()
    with conn.cursor() as cur:
        cur.execute(
            "DELETE FROM students WHERE student_id = %s;",
            (student_id,)
        )
        conn.commit()
    conn.close()

# Main function to run your application functions
def main():
    while True:
        print("Choose an option:")
        print("1: Get all students")
        print("2: Add a student")
        print("3: Update a student's email")
        print("4: Delete a student")
        print("5: Exit")
        
        choice = input("Enter the number of your choice: ")
        
        if choice == '1':
            getAllStudents()
        elif choice == '2':
            first_name = input("Enter student's first name: ")
            last_name = input("Enter student's last name: ")
            email = input("Enter student's email: ")
            enrollment_date = input("Enter student's enrollment date (YYYY-MM-DD): ")
            addStudent(first_name, last_name, email, enrollment_date)
            print("Student added successfully.")
        elif choice == '3':
            student_id = int(input("Enter the student's ID to update their email: "))
            new_email = input("Enter the new email: ")
            updateStudentEmail(student_id, new_email)
            print("Email updated successfully.")
        elif choice == '4':
            student_id = int(input("Enter the student's ID to delete their record: "))
            deleteStudent(student_id)
            print("Student deleted successfully.")
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")
            
        print("\n")  # Print a new line for better readability after an action is completed

if __name__ == "__main__":
    main()
