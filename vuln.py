from flask import Flask, request, render_template_string
import sqlite3

app = Flask(__name__)

# Database setup (for demonstration purposes only)
def init_db():
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)')
    cursor.execute('INSERT INTO users (username, password) VALUES ("admin", "password123")')
    conn.commit()
    conn.close()

# Initialize the database
init_db()

@app.route('/')
def index():
    return "Welcome to the Vulnerable Flask App!"

# SQL Injection Vulnerability
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        conn = sqlite3.connect('example.db')
        cursor = conn.cursor()
        
        # Vulnerable to SQL Injection
        cursor.execute(f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'")
        
        user = cursor.fetchone()
        conn.close()
        
        if user:
            return "Login Successful!"
        else:
            return "Invalid Credentials!"
    return '''
        <form method="post">
            Username: <input type="text" name="username"><br>
            Password: <input type="password" name="password"><br>
            <input type="submit" value="Login">
        </form>
    '''

# XSS Vulnerability
@app.route('/greet')
def greet():
    name = request.args.get('name', 'Guest')
    return render_template_string(f"<h1>Hello, {name}!</h1>")

# Improper Error Handling
@app.route('/divide')
def divide():
    try:
        a = int(request.args.get('a', '1'))
        b = int(request.args.get('b', '0'))
        result = a / b
        return f"Result: {result}"
    except Exception as e:
        return str(e), 500

if __name__ == '__main__':
    app.run(debug=True)
