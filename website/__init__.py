from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
import os
from dotenv import load_dotenv
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = "database.db"
login_manager = LoginManager()


def create_app():
    load_dotenv()  # Load from .env file

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
    db.init_app(app)
    
    
    from .views import views
    from .auth import auth
    
    app.register_blueprint(views, url_prefix ='/')
    app.register_blueprint( auth, url_prefix ='/')
    
    from .models import User, Note
    create_database(app)

    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)


    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))
        
    return app

def create_database(app):
    if not path.exists('website/' + DB_NAME):  
        with app.app_context():                
            db.create_all()
            print('Created Database!')

    