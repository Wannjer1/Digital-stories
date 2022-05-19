from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,TextAreaField,ValidationError,RadioField
from wtforms.validators import InputRequired,Email
from ..models import User
from flask_login import current_user

class UpdateProfile(FlaskForm):
    username = StringField('New username',validators = [InputRequired()])
    email = StringField('New email',validators = [InputRequired(),Email()])
    bio = TextAreaField('Tell us about you.',validators = [InputRequired()])
    submit = SubmitField('Submit')

    def validate_email(self,email):
        if email.data != current_user.email:
            if User.query.filter_by(email = email.data).first():
                raise ValidationError("The Email has already been taken!")
    
    def validate_username(self, username):
        if username.data != current_user.username:
            if User.query.filter_by(username = username.data).first():
                raise ValidationError("The username has already been taken")

# form to enable creation of new blog post
class CreateBlog(FlaskForm):
    title = StringField('Title',validators=[InputRequired()])
    author = StringField('Author',validators=[InputRequired()])
    category = RadioField('Category', choices=[('Fashion','Fashion'),('Food','Food'),('Interior_Design','Interior_Design'),('Lifestyle','Lifestyle'),('')],validators=[InputRequired()])
    content = TextAreaField('Blog Content',validators=[InputRequired()])
    submit = SubmitField('Post')