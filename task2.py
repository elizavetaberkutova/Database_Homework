
import sqlite3

conn = sqlite3.connect("hospital.db")
cursor = conn.cursor()

cursor.executescript("""
CREATE TABLE IF NOT EXISTS Departments (
    Id INTEGER PRIMARY KEY AUTOINCREMENT,
    Building INTEGER NOT NULL CHECK(Building BETWEEN 1 AND 5),
    Financing REAL NOT NULL DEFAULT 0 CHECK(Financing >= 0),
    Name TEXT NOT NULL UNIQUE CHECK(length(trim(Name)) > 0)
);

CREATE TABLE IF NOT EXISTS Diseases (
    Id INTEGER PRIMARY KEY AUTOINCREMENT,
    Name TEXT NOT NULL UNIQUE CHECK(length(trim(Name)) > 0),
    Severity INTEGER NOT NULL DEFAULT 1 CHECK(Severity >= 1)
);

CREATE TABLE IF NOT EXISTS Doctors (
    Id INTEGER PRIMARY KEY AUTOINCREMENT,
    Name TEXT NOT NULL CHECK(length(trim(Name)) > 0),
    Phone TEXT CHECK(Phone IS NULL OR length(Phone) = 10),
    Salary REAL NOT NULL CHECK(Salary > 0),
    Surname TEXT NOT NULL CHECK(length(trim(Surname)) > 0)
);

CREATE TABLE IF NOT EXISTS Examinations (
    Id INTEGER PRIMARY KEY AUTOINCREMENT,
    DayOfWeek INTEGER NOT NULL CHECK(DayOfWeek BETWEEN 1 AND 7),
    EndTime TEXT NOT NULL,
    Name TEXT NOT NULL UNIQUE CHECK(length(trim(Name)) > 0),
    StartTime TEXT NOT NULL
        CHECK(StartTime BETWEEN '08:00' AND '18:00'),
    CHECK(EndTime > StartTime)
);

CREATE TABLE IF NOT EXISTS Wards (
    Id INTEGER PRIMARY KEY AUTOINCREMENT,
    Building INTEGER NOT NULL CHECK(Building BETWEEN 1 AND 5),
    Floor INTEGER NOT NULL CHECK(Floor >= 1),
    Name TEXT NOT NULL UNIQUE CHECK(length(trim(Name)) > 0)
);
""")

conn.commit()
conn.close()

print("Базу даних Hospital створено!")


conn = sqlite3.connect("hospital.db")
cursor = conn.cursor()

cursor.execute(
    "SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%'"
)

for table in cursor.fetchall():
    print(table[0])

conn.close()


conn = sqlite3.connect("hospital.db")
cursor = conn.cursor()

tables = [
    "Departments",
    "Diseases",
    "Doctors",
    "Examinations",
    "Wards"
]

for table in tables:
    print("\nТаблиця:", table)

    cursor.execute(f"PRAGMA table_info({table})")

    for column in cursor.fetchall():
        print(column[1])

conn.close()



conn = sqlite3.connect("hospital.db")
cursor = conn.cursor()

try:
    cursor.execute("""
        INSERT INTO Departments (Building, Name)
        VALUES (10, 'Test')
    """)
    conn.commit()
    print("Помилка: неправильні дані додано!")
except sqlite3.IntegrityError:
    print("Перевірка успішна! Корпус 10 заборонено.")

conn.close()
