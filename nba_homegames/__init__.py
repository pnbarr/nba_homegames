from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = 'fac97d332b5b472f5f509009eba1b419'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'  #  Relative path from this file
db = SQLAlchemy(app)  #  SQLAlchemy database instance
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

from nba_homegames import routes