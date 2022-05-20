from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin, current_user
from datetime import datetime
from . import db,login_manager


class Quote():
  def __init__(self,author,quote):
    self.author = author
    self.quote = quote

@login_manager.user_loader
def load_user(user_id):
  return User.query.get(int(user_id))


class User(UserMixin, db.Model):
  __tablename__ = 'users'
  
  id = db.Column(db.Integer, primary_key=True)
  first_name = db.Column(db.String(255))
  last_name = db.Column(db.String(255))
  username = db.Column(db.String(255), unique=True, index=True)
  email = db.Column(db.String(255), unique=True, index=True)
  bio = db.Column(db.String(255))
  profile_pic_path = db.Column(db.String(255))
  password_hash = db.Column(db.String(255))
  role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
  blog_id = db.relationship('Blog',backref='user', lazy='dynamic')
  # comments = db.relationship('Comments',backref='comments', lazy='dynamic')
  
  @property
  def password(self):
    raise AttributeError('you cannot read the password')
  
  @password.setter
  def password(self, password):
    '''Method to create a hashed password'''
    self.password_hash = generate_password_hash(password)
    
  def verify_password(self, password):
    '''Method to verify if a password is hashed'''
    return check_password_hash(self.password_hash, password)
  
  def __repr__(self):
      return f'User {self.username}'

    
# model for roles
class Role(db.Model):
  __tablename__ = 'roles'
  id = db.Column(db.Integer, primary_key=True)
  name= db.Column(db.String(255))
  users = db.relationship('User',backref = 'role', lazy = "dynamic")

  def __repr__(self):
    return f'User {self.name}'

  # blog class

class Blog(db.Model):
  ''''''
  __tablename__ = 'blogs'

  id = db.Column(db.Integer, primary_key = True)
  # blog_image= db.Column(db.String,nullable=False)
  title = db.Column(db.String(255))
  category = db.Column(db.String())
  owner_id = db.Column(db.Integer,db.ForeignKey("users.id"))
  posted = db.Column(db.DateTime,default=datetime.utcnow)
  description = db.Column(db.String(), index = True)
  comments = db.relationship('Comments', backref='blog', lazy = 'dynamic')

  def save_blog(self):
    db.session.add(self)
    db.session.commit()


  def __repr__(self):
    return f'Blog {self.title}'

# comments model
class Comments(db.Model):
  __tablename__ = 'comments'
  id = db.Column(db.Integer,primary_key=True)
  comment = db.Column(db.String(), nullable=False)
  blog_id = db.Column(db.Integer,db.ForeignKey('blogs.id'))
  user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
 

  def save_comment(self):
    db.session.add(self)
    db.session.commit()


  @classmethod
  def get_comment(cls,blog_id):
    comments = Comments.query.filter_by(blog_id=blog_id)
    return comments

  def __repr__(self):
    return f'Comments {self.comment}'