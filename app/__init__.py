from flask import Flask
from config import config_options



def create_app(config_name):
   app = Flask(__name__)
   
   #create the app configurations
   app.config.from_object(config_options[config_name])
   config_options[config_name].init_app(app)
   

#import the blueprints
   from .main import main as main_blueprint
   from . auth import auth as auth_blueprint
#register the blueprints
   app.register_blueprint(main_blueprint)
   app.register_blueprint(auth_blueprint,url_prefix='/user-account')

   return app