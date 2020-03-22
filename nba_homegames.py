from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'fac97d332b5b472f5f509009eba1b419'
app.config['SQLALCHEMY_DATABASE_UR'] = 'sqlite:///site.db'  # relative path from this file
db = SQLAlchemy(app)  #SQLAlchemy database instance

# User class for table in database
class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(20), unique = True, nullable =  False)
    email = db.Column(db.String(120), unique = True, nullable =  False)
    image_file = db.Column(db.String(20), nullable =  False, default = 'default.jpg')
    password = db.Column(db.String(60), nullable = False)  # 60 character because of hashing algorithm
    posts = db.relationship('Post', backref = 'author', lazy = True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"

# Post class for table in database
class Post(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100), nullable = False)
    date_posted = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)
    content = db.Column(db.Text, nullable = False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"



teams = [
    {
        'city' : 'Atlanta',
        'name' : 'Hawks'
    },
    {
        'city' : 'Boston',
        'name' : 'Celtics'
    },
    {
        'city' : 'Brooklyn',
        'name' : 'Nets'
    },
    {
        'city' : 'Charlotte',
        'name' : 'Hornets'
    },
    {
        'city' : 'Chicago',
        'name' : 'Bulls'
    },
    {
        'city' : 'Cleveland',
        'name' : 'Cavaliers'
    },
    {
        'city' : 'Dallas',
        'name' : 'Mavericks'
    },
    {
        'city' : 'Denver',
        'name' : 'Nuggets'
    },
    {
        'city' : 'Detroit',
        'name' : 'Pistons'
    },
    {
        'city' : 'Golden State',
        'name' : 'Warriors'
    },
    {
        'city' : 'Houston',
        'name' : 'Rockets'
    },
    {
        'city' : 'Indiana',
        'name' : 'Pacers'
    },
    {
        'city' : 'LA',
        'name' : 'Clippers'
    },
    {
        'city' : 'LA',
        'name' : 'Lakers'
    },
    {
        'city' : 'Memphis',
        'name' : 'Grizzlies'
    },
    {
        'city' : 'Miami',
        'name' : 'Heat'
    },
    {
        'city' : 'Milwaukee',
        'name' : 'Bucks'
    },
    {
        'city' : 'Minnesota',
        'name' : 'Timberwolves'
    },
    {
        'city' : 'New Orleans',
        'name' : 'Pelicans'
    },
    {
        'city' : 'New York',
        'name' : 'Knicks'
    },
    {
        'city' : 'Oklahoma City',
        'name' : 'Thunder'
    },
    {
        'city' : 'Orlando',
        'name' : 'Magic'
    },
    {
        'city' : 'Philadelphia',
        'name' : '76ers'
    },
    {
        'city' : 'Phoenix',
        'name' : 'Suns'
    },
    {
        'city' : 'Portland',
        'name' : 'Trailblazers'
    },
    {
        'city' : 'Sacramento',
        'name' : 'Kings'
    },
    {
        'city' : 'San Antonio',
        'name' : 'Spurs'
    },
    {
        'city' : 'Toronto',
        'name' : 'Raptors'
    },
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', teams=teams)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/register', methods = ['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title = 'Register', form =  form)

@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have beend logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title = 'Login', form =  form)