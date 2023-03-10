from flask import render_template
from app import app
from app.forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Luis'}
    posts = [
        {
            'author': {'username': 'Barry Allen'},
            'body': 'Being the fastest man in the world is not easy!'
        },
        {
            'author': {'username': 'John Stewart'},
            'body': '''In brightest day, in blackest night,
                        No evil shall escape my sight.
                        Let those who worship evil's might,
                        Beware my power... Green Lantern's light! '''
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)


@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)
