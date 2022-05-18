from flask import render_template,request,redirect,url_for,abort
from flask_login import login_required, current_user
from ..models import User
from datetime import datetime as dt
from forms import UpdateProfile
from .. import db

from .. import db,photos
from . import main

@main.route('/', methods= ['GET','POST'])
@login_required
def index():
  '''function that renders the homepage'''
  title = 'One place, Many Stories'
 
  return render_template('index.html', title=title)

# view function for displaying profile page
@main.route('/user/<uname>')
def profile(uname):
  user = User.query.filter_by(username=uname).first()

  if user is None:
    abort(404)

  return render_template('profile/profile.html', user=user)

# view profile for updating profile
@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data
        user.username = form.username.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)