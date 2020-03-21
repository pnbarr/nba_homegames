from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = 'fac97d332b5b472f5f509009eba1b419'

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