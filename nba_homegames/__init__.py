from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from nba_homegames.config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)  #  SQLAlchemy database instance
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'
mail = Mail(app)

from nba_homegames.users.routes import users
from nba_homegames.posts.routes import posts
from nba_homegames.main.routes import main

app.register_blueprint(users)
app.register_blueprint(posts)
app.register_blueprint(main)