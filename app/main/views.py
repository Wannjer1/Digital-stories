from flask import render_template,request,redirect,url_for,abort
from flask_login import login_required, current_user
from ..models import Comments, User,Blog,Role
from datetime import datetime as dt
from .forms import UpdateProfile,CreateBlog,CommentForm
from .. import db,photos
from .. email import mail_message
from ..requests import get_quote
from . import main
from app.main import main
import os 



@main.route('/', methods= ['GET','POST'])
@login_required
def index():
  '''function that renders the homepage'''
  quote = get_quote()


  title = 'One place, Many Stories'
  Fashion = Blog.query.filter_by(category='Fashion')
  Food = Blog.query.filter_by(category='Food')
  Lifestyle = Blog.query.filter_by(category='Lifestyle')
  Interior_Design = Blog.query.filter_by(category='Interior_Design')
  blogs = Blog.query.all()
  


 
  return render_template('index.html', title=title,quote=quote,blogs=blogs,Food=Food,Interior_Design=Interior_Design,Fashion=Fashion,Lifestyle=Lifestyle)

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

@main.route('/newBlog', methods=['GET','POST'])
@login_required
def new_blog():
  newblog_form = CreateBlog()
  # user = current_user

  if newblog_form.validate_on_submit():
    title = newblog_form.title.data
    category = newblog_form.category.data
    content = newblog_form.content.data
    # print(current_user._get_current_object().id)
    new_blog = Blog(owner_id=current_user.id,title=title,category=category,content=content)
    db.session.add(new_blog)
    db.session.commit()


    return redirect(url_for('main.index'))
  return render_template('newblog.html',form=newblog_form)

# delete and edit blog post 

# @main.route('/edit_post/<int:pitch_id>', methods=['GET','POST'])
# @login_required
# def update_post(pitch_id):
#     pitch = Pitches.query.filter_by(id=pitch_id).first()

#     form = UpdatePost()
#     if form.validate_on_submit():
#         pitch.text=form.text.data
#         db.session.add(pitch)
#         db.session.commit()
#         return redirect(url_for('.home', pitch_id=pitch.id))
#     return render_template('edit_post.html', form=form)


# @main.route('/delete_post/<int:pitch_id>', methods=['GET','POST'])
# @login_required
# def delete_post(pitch_id):
#     pitch = Pitches.query.filter_by(id=pitch_id).first()

#     db.session.delete(pitch)
#     db.session.commit()
#     return redirect(url_for('.home', pitch_id=pitch.id))

  # view root to enable commenting
@main.route('/comments/<int:blog_id>', methods=['GET','POST'])
def blog_comments(blog_id):
  comments = Comments.get_comments(blog_id)

  blog = Blog.query.get(blog_id)
  blog_posted_by = blog.user_id
  user = User.query.filter_by(id=blog_posted_by).first()
  form = CommentForm()

  if form.validate_on_submit():
    comment = form.blog_comments.data
    new_comment = Comments(comment = comment,blog_id = blog_id,user_id = current_user.get_id())
    new_comment.save_comment()

    return redirect(url_for('main.blog_comments',blog_id=blog_id))

  return render_template('comments.html',comment_form=form,comments=comments,blog = blog, user = user)


@main.route('/delete_comment/<int:comment_id>', methods=['GET','POST'])
@login_required
def delete_comment(comment_id):
    comment = Comments.query.filter_by(id=comment_id).first()

    db.session.delete(comment)
    db.session.commit()
    return redirect(url_for('.main', comment_id=comment.id))