import os

class Config:
  '''class to configure url parameters'''
  SECRET_KEY = os.environ.get('SECRET_KEY')
  SQLALCHEMY_TRACK_MODIFICATIONS = False
  UPLOADED_PHOTOS_DEST ='app/static/photos'
  MAIL_SERVER = 'smtp.googlemail.com'
  MAIL_PORT = 587
  MAIL_USE_TLS = True
  MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
  MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
  
class ProdConfig(Config):
  # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
  # if SQLALCHEMY_DATABASE_URI.startswith("postgres://"): 
  #   SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI.replace("postgres://", "postgresql://", 1)
  pass


class DevConfig(Config):
  SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://wanjeri:pass123@localhost:5432/modernblog'
  DEBUG = True
 
  
config_options = {
  'development': DevConfig,
  'production': ProdConfig,
  
}
  