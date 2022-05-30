
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = "database.db"


def create_app():   #definování funkce
    app = Flask(__name__) #__name__ reprezentuje jmeno souboru, inizicalizace flasku
    app.config['SECRET_KEY'] = 'kakskfjkds skxjdkdnvvs' #pro všechny flask potřebujeme proměnou zvanou secret, šifruje či zabezpečuje cookies a data o relacích související s webem, sksdhf je secret key
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    from .views import views #importování složeky a importování blueprint
    from .auth import auth #importování složky a importování blueprint

    app.register_blueprint(views, url_prefix='/') #registrování blueprint z views,
    app.register_blueprint(auth, url_prefix='/') #registrování blueprint z auth, no prefex to znamená

    from .models import User, Note

    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app


def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')

