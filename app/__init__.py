from flask_login import LoginManager
from flask import Flask
from .models import db, User

# Register blueprints
from .auth import auth as auth_blueprint
from .main import main as main_blueprint
from .dashboard import dashboard as dashboard_blueprint

login_manager = LoginManager()
login_manager.login_view = 'auth.login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    # Initialize extensions
    db.init_app(app)
    login_manager.init_app(app)

    app.register_blueprint(main_blueprint)
    app.register_blueprint(dashboard_blueprint, url_prefix='/dashboard')
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    return app
