from flask import render_template
from . import app

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/catalog')
def catalog():
    return render_template('catalog.html')

@app.route('/profile')
def profile():
    return "<h1>Profile Page</h1><p>Placeholder for user profile.</p>"

@app.route('/login', methods=['GET', 'POST'])
def login():
    return "<h1>Login Page</h1><p>Placeholder for login form.</p>"

@app.route('/register', methods=['GET', 'POST'])
def register():
    return "<h1>Register Page</h1><p>Placeholder for registration form.</p>"

@app.route('/book/<int:book_id>')
def book_details(book_id):
    return f"<h1>Book Details</h1><p>Placeholder for book {book_id} details.</p>"

