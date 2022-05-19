
from unicodedata import category
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin, current_user
from datetime import datetime
from . import db,login_manager

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
  role_id = db.Column(db.Integer,db.ForeignKey('roles.id'),nullable=False)
  blog_user = db.relationship('Blog',backref='user', lazy='dynamic')
 
  
  @property
  def password(self):
    raise AttributeError('you cannot read the password')
  
  @password.setter
  def password(self, password):
    self.password_hash = generate_password_hash(password)
    
  def verify_password(self, password):
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
  blog_image= db.Column(db.String,nullable=False)
  title = db.Column(db.String(255),nullable=False)
  category = db.Column(db.String(255),nullable=False)
  owner_id = db.Column(db.Integer,db.ForeignKey("users.id"),nullable=False)
  posted = db.Column(db.DateTime,default=datetime.utcnow,nullable=False)
  content = db.Column(db.String(),nullable=False)
  

  def save_blog(self):
    db.session.add(self)
    db.session.commit()

#   # def delete(self):
#   #   db.session.delete(self)
#   #   db.session.commit()

#   # def get_blog(id):
#   #   blog = Blog.query.filter_by(id=id).first()
#   #   return blog

  # @classmethod
  # def get_blog(cls, id):
  #   blogs = Blog.query.filter_by(id=id).first()
  #   return blogs

  def __repr__(self):
    return f'Blog {self.category}'

# comments model
# class Comment(db.Model):
#   __tablename__ = 'comments'
#   id = db.Column(db.Integer,primary_key=True)
#   comment = db.Column(db.String)
#   posted = db.Column(db.DateTime,default=datetime.datetime.utcnow)
#   blog_id = db.Colun(db.Integer,db.ForeignKey('blogs.id'))
#   user_id = db.Column(db.Integer,db.ForeignKey('users.id'))

#   def save(self):
#     db.session.add(self)
#     db.session.commit()

#   def delete(self):
#     db.session.remove(self)
#     db.session.commit()

#   def get_comment(id):
#     comment = Comment.query.all(id=id)
#     return comment

#   def __repr__(self):
#     return f'Comment {self.comment}'



    