from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SECRET_KEY'] = 'fac97d332b5b472f5f509009eba1b419'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'  # relative path from this file
db = SQLAlchemy(app)  #SQLAlchemy database instance
bcrypt = Bcrypt(app)

from nba_homegames import routes