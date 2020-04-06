from flask import Blueprint, render_template, request
from nba_homegames.models import Post
from nba_homegames.main.forms import DateEntryForm

main = Blueprint('main', __name__)


@main.route('/')
@main.route('/home')
def home():
    page = request.args.get('page', 1, type = int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page = page, per_page = 5)
    return render_template('home.html', posts = posts)

@main.route('/about')
def about():
    return render_template('about.html')

@main.route('/search', methods = ['GET', 'POST'])
def search():
    start_search_form = DateEntryForm(id='startdate')
    stop_search_form = DateEntryForm(id='stopdate')
    return render_template('search.html', start_search_form=start_search_form, stop_search_form=stop_search_form)