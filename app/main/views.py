from flask import render_template,request,redirect,url_for,abort
from flask_login import login_required, current_user
from ..models import User,Blog,Role
from datetime import datetime as dt
from .forms import UpdateProfile,CreateBlog
from .. import db,photos
from .. email import mail_message
from . import main
from app.main import main
import os 



@main.route('/', methods= ['GET','POST'])
@login_required
def index():
  '''function that renders the homepage'''
  title = 'One place, Many Stories'
  Fashion = Blog.query.filter_by(category='Fashion')
  Food = Blog.query.filter_by(category='Food')
  Lifestyle = Blog.query.filter_by(category='Lifestyle')
  Interior_Design = Blog.query.filter_by(category='Interior_Design')
  blogs = Blog.query.all()
  


 
  return render_template('index.html', title=title,blogs=blogs,Food=Food,Interior_Design=Interior_Design,Fashion=Fashion,Lifestyle=Lifestyle)

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


# view route for updating profile picture
@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))



# view root for the new blogs

@main.route('/newBlog ', methods=['GET','POST'])
@login_required
def new_blog():
  form = CreateBlog()
  user = current_user

  if form.validate_on_submit():
    title = form.title.data
    author = form.author.data
    category = form.category.data
    content = form.content.data
    owner_id = current_user._get_current_object().id
    new_blog = Blog(owner_id=current_user._get_current_object().id,title=title,category=category,content=content,author=author)
    db.session.add(new_blog)
    db.session.commit()


    return redirect(url_for('main.index'))
  return render_template('newblog.html',form=form,user=user)
