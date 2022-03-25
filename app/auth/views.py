from . import auth
from flask import render_template

@auth.route('/login')
def login():
  

  title = "login"
  return render_template('auth/login.html',title=title)

@auth.route('/signup')
def signup():
  

  title = "signup"
  return render_template('auth/signup.html',title=title)