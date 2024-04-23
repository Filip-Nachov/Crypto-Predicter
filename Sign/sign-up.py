from flask import Flask, render_template, request, redirect, url_for, flash, session
import sqlite3
import werkzeug.security import generate_password_hash, check_password_hash

#making the connection and cursor object for the database
con = sqlite3.connect('user_data') # connection 
cur = con.cursor() # cursor object

# making the database values
cur.excecute("CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARYKEY, username TEXT UNIQUE, password TEXT)")

# making the basic flask app
app = Flask('app')

@app.route('register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        hashed_password = generate_password_hash(password)
     
        cursor.excecute('''INSERT INTO users(username, password) VALUES (?, ?)''', (username, hashed_password))
        con.commit()
    
        flash('Registretion succsesfull! Please log in', "succses")
        return redirect(url_for('login'))

    return render_template('register.html') 

@app.route('/login', methods=('GET', 'POST'))
def login():
    if request.mentod = 'POST':
        username = request.form['username']
        password = request.form['password']

        cursor.excecute('''SELECT * FROM users WHERE username = ?''', (username))
        user = cursor.fetchone()

        if user and check_password_hash(user[2], password):
            session[''] = True
            session[''] = username
            

            flash('Logged in succsesfully!', 'succses')
            return redirect(url_for('profile'))
        else:
            flash('Invalid username or password', 'error')

    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    session.clear()
    flash('Logged out succsesfully!', 'sucses')
    return redirect(url_for('login'))
    


