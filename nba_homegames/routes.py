from flask import Flask, render_template, url_for, flash, redirect, request
from nba_homegames.forms import RegistrationForm, LoginForm
from nba_homegames.models import User,Post
from nba_homegames import app, db, bcrypt
from flask_login import login_user, current_user, logout_user, login_required

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
    #  Redirect to home if user is already logged in
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username = form.username.data, email = form.email.data, password = hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created, you are now able to log in!', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title = 'Register', form =  form)

@app.route('/login', methods = ['GET', 'POST'])
def login():
    #  Redirect to home if user is already logged in
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email = form.email.data).first()
        #  If user exists in database and password matches
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember =  form.remember.data)
            next_page =  request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title = 'Login', form =  form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/account')
@login_required
def account():
    return render_template('account.html', title = 'Account')

