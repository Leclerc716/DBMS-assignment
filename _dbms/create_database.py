import sqlite3
import pandas as pd

# Path to your CSV file
csv_file_path = 'collegedunia_cleaned.csv'

# Load CSV data
data = pd.read_csv(csv_file_path)

# Clean and format 'Fees' column to store as an integer
data['Fees'] = data['Fees'].replace('[₹,]', '', regex=True).astype(int)

# Connect to SQLite database (will create the database file if it doesn't exist)
database_path = 'engineering_colleges.db'
conn = sqlite3.connect(database_path)

# Create a new SQLite table for the college data
create_table_query = """
CREATE TABLE IF NOT EXISTS colleges (
    College_Name TEXT,
    Location TEXT,
    Fees INTEGER,
    College_URL TEXT
);
"""
conn.execute(create_table_query)
conn.commit()

# Insert data from DataFrame into the table
data.to_sql('colleges', conn, if_exists='replace', index=False)

# Close the connection
conn.close()

print("Database created and data loaded successfully!")
