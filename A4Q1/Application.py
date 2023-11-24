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
    #getAllStudents()
    #addStudent('Karim', 'Fouad', 'karim@example.com', '2023-09-03')
    #updateStudentEmail(25, 'jimmyJimGym@gymmer.com')
    #deleteStudent(26)

    
if __name__ == "__main__":
    main()
