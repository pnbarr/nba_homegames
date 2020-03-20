from flask import Flask, render_template, url_for
app = Flask(__name__)

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