from flask import Flask, render_template, redirect, url_for, session, request
import sqlite3
import create_database
app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a secure key in production

# Function to get colleges from the database
def get_nursing_colleges():
    # Connect to the updated database file, 'engineering_colleges.db'
    conn = sqlite3.connect('engineering_colleges.db')
    cursor = conn.cursor()
    
    # Update query to retrieve all relevant columns (excluding ID)
    cursor.execute('SELECT College_Name, Location, Fees, College_URL FROM colleges')
    colleges = cursor.fetchall()
    
    conn.close()
    #print(colleges) 
    return colleges

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/home', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Simple authentication check for demonstration purposes
        if username and password:
            session['username'] = username
            return redirect(url_for('home'))

    if 'username' not in session:
        return redirect(url_for('login'))

    colleges = get_nursing_colleges()  # Fetch colleges from the database
    #print("Colleges data in home route:", colleges)  # Debugging line
    return render_template('home.html', colleges=colleges)  # Pass the college data to the template

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    create_database
    app.run(debug=True)
