from flask import Flask
from config import config_options
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

bootstrap=Bootstrap()
db=SQLAlchemy()
# photos = UploadSet('photos',IMAGES)

# login_manager = LoginManager()
 
# login_manager.session_protection = 'strong'
# login_manager.login_view = 'auth.login'


def create_app(config_name):
   app = Flask(__name__)
   
   #create the app configurations
   app.config.from_object(config_options[config_name])
   config_options[config_name].init_app(app)
   
   # Initializing flask extensions
   db.init_app(app)
   bootstrap.init_app(app)
   # login_manager.init_app(app)
   
#import the blueprints
   from .main import main as main_blueprint
   from . auth import auth as auth_blueprint
#register the blueprints
   app.register_blueprint(main_blueprint)
   app.register_blueprint(auth_blueprint,url_prefix='/user-account')

   return app