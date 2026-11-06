
import sqlite3

conn = sqlite3.connect("students.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS StudentGrades (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    full_name TEXT NOT NULL,
    city TEXT,
    country TEXT,
    birth_date TEXT,
    email TEXT,
    phone TEXT,
    group_name TEXT,
    average_grade REAL,
    min_subject TEXT,
    max_subject TEXT
)
""")

conn.commit()
conn.close()

print("Базу даних студентів створено!")


conn = sqlite3.connect("students.db")
cursor = conn.cursor()

cursor.execute(
    "SELECT name FROM sqlite_master WHERE type='table' AND name='StudentGrades'"
)

for table in cursor.fetchall():
    print(table[0])

conn.close()


conn = sqlite3.connect("students.db")
cursor = conn.cursor()

cursor.execute("PRAGMA table_info(StudentGrades)")

for column in cursor.fetchall():
    print(column[1])

conn.close()
