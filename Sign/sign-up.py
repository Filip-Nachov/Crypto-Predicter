from flask import Flask, render_template, request, redirect, url_for, flash, session, jsonify
import sqlite3
import werkzeug.security
from werkzeug.security import generate_password_hash, check_password_hash

#making the connection and cursor object for the database
con = sqlite3.connect('user_data') # connection 
cur = con.cursor() # cursor object

# making the database values
cur.execute("CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARYKEY, username TEXT UNIQUE, password TEXT)")

# making the basic flask app
app = Flask('app')

@app.route('/data', methods=['GET'])
def get_data():
    data = {'message': 'Hello from Flask!'}
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        hashed_password = generate_password_hash(password)
     
        cursor.excecute('''INSERT INTO users(username, password) VALUES (?, ?)''', (username, hashed_password))
        con.commit()
    
        flash('Registretion succsesfull! Please log in', "success")
        return redirect(url_for('login'))

    return render_template('signup.html') 

@app.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        cursor.execute('''SELECT * FROM users WHERE username = ?''', (username))
        user = cursor.fetchone()

        if user and check_password_hash(user[2], password):
            session['logged_in'] = True
            session['username'] = username
            

            flash('Logged in succsesfully!', 'success')
            return redirect(url_for('profile'))
        else:
            flash('Invalid username or password', 'error')

    return render_template('login.html')

def login_required(func):
    def wrapper(*args, **kwargs):
        if 'logged_in' in session:
            return func(*args, **kwargs)
        else:
            flash('You need to be logged in to access this page', 'error')
            return redirect(url_for('login'))
    return wrapper

@app.route('/profile')
@login_required
def profile():
    return render_template('profile.html')

    


