import sqlite3

conn = sqlite3.connect('mydatatbase.db')
cur = conn.cursor()
cur.execute( '''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        city TEXT NOT NULL
    )
''')

cur.execute("INSERT INTO users (name, age, city) VALUES ('Alice, 25, 'New York')")
cur.execute("INSERT INTO users (name, age, city) VALUES (')")