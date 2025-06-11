from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
import os
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = "database.db"
login_manager = LoginManager()


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    app.secret_key = 'JDFortiTech'
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

# def create_database(app):
#     db_path = os.path.join('website', DB_NAME)
#     full_path = os.path.abspath(db_path)
#     print(f"Looking for database at: {full_path}")

#     if not path.exists(db_path):
#         print("Database does not exist. Creating...")
#         with app.app_context():
#             db.create_all()
#             print(f'✅ Created Database at: {full_path}')
#     else:
#         print("Database already exists.")

    