from flask import Blueprint

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return '<p>This is your login page</p>'

@auth.route('/logout')
def logout():
    return '<p>This is where you logout from</p>'

@auth.route('/sign-up')
def sign_up():
    return '<p>Sign Up here</p>'