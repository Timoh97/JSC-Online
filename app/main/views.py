from flask import render_template
from . import main

@main.route('/index')
def index():
  

  title = "Home page"
  return render_template('main/index.html',title=title)

@main.route('/profile')
def profile():
  

  title = "profile page"
  return render_template('profile/profile.html',title=title)