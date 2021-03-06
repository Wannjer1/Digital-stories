
from flask import Flask
from config import config_options
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_uploads import UploadSet,configure_uploads,IMAGES
from flask_mail import Mail
from flask_bootstrap import Bootstrap

db = SQLAlchemy()
mail = Mail()
photos = UploadSet('photos',IMAGES)
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'
bootstrap = Bootstrap()



def create_app(config_name):
  '''function to create and configure the Flask app'''
  app = Flask(__name__)

  #Creating the app configurations
  app.config.from_object(config_options[config_name])
  
  #Initializing flask extension
  db.init_app(app)
  login_manager.init_app(app)
  configure_uploads(app,photos)
  mail.init_app(app)
  bootstrap.init_app(app)

      #Registering the blueprint
  '''import and register the main blueprint'''
  from .main import main as main_blueprint
  app.register_blueprint(main_blueprint)
  
    # registering the auth blueprint
  from .auth import auth as auth_blueprint
  app.register_blueprint(auth_blueprint, url_prefix='/authenticate')
  
  '''import and configure the requests for use in the app'''
  # from .requests import configure_request
  # configure_request(app)
  
  
  return app