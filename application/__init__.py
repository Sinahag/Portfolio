from flask import Flask, render_template
from config import Config
from flask_mongoengine import MongoEngine
from flask_login import LoginManager


db = MongoEngine()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    from application.auth.models import User

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    db.init_app(app)

    @login_manager.user_loader
    def user_loader(user_id):
        return User.objects(id=user_id).first()

    @app.errorhandler(404)
    def not_found(error):
        return render_template('/errors/404.html')

    from application.auth.auth import auth as auth_blueprint

    app.register_blueprint(auth_blueprint)

    from application.main.main import main as main_blueprint

    app.register_blueprint(main_blueprint)

    return app

