from flask import render_template,request,redirect,url_for,abort
from flask_login import login_required, current_user
from datetime import datetime as dt

from .. import db,photos
from . import main

@main.route('/', methods= ['GET','POST'])
@login_required
def index():
  '''function that renders the homepage'''
  title = 'One place, Many Stories'
 
  return render_template('index.html', title=title)