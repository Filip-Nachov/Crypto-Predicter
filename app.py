from flask import Flask, render_template, url_for 
from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, static_folder='static')
app.config['SECRET_KEY'] = 'H1$sda'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(80), nullable=False)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('signup.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/purchases')
def purchases():
    return render_template('purchases.html')

@app.route('/editprofile')
def editprofile():
    return render_template('editprofile.html')

@app.route('/crypto')
def crypto():
    return render_template('crypto.html')

if __name__ == "__main__":
    app.run(debug=True, port=80)
