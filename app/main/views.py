from flask import render_template,request,redirect,url_for,abort
from flask_login import login_required, current_user
from ..models import User
from datetime import datetime as dt

from .. import db,photos
from . import main

@main.route('/', methods= ['GET','POST'])
@login_required
def index():
  '''function that renders the homepage'''
  title = 'One place, Many Stories'
 
  return render_template('index.html', title=title)

@main.route('/user/<uname>')
def profile(uname):
  user = User.query.filter_by(username=uname).first()

  if user is None:
    abort(404)

  return render_template('profile/profile.html', user=user)