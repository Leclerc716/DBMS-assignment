import sqlite3

conn = sqlite3.connect('engineering_colleges.db')
cursor = conn.cursor()

# Check if the table exists and display some data
try:
    cursor.execute('SELECT * FROM colleges LIMIT 5;')
    rows = cursor.fetchall()
    if rows:
        print("Data found:", rows)
    else:
        print("No data found in the table.")
except Exception as e:
    print("Error:", e)

conn.close()
