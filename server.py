from flask import Flask, request, render_template 
from flask import session, url_for, redirect, abort, flash
from form import LoginForm
from config import OPENID_PROVIDERS

app = Flask(__name__)
app.config['SECRET_KEY']='F3T%$@XXX'
app.config['OPENID_PROVIDERS'] = [
    {'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id'},
    {'name': 'Yahoo', 'url': 'https://me.yahoo.com'},
    {'name': 'AOL', 'url': 'http://openid.aol.com/<username>'},
    {'name': 'Flickr', 'url': 'http://www.flickr.com/<username>'},
    {'name': 'MyOpenID', 'url': 'https://www.myopenid.com'}]

@app.route('/')
def home():
	user = {'name': 'James'}
	posts = [  # fake array of posts
        { 
            'author': 'James',
            'date': 'December 27 2014', 
            'title': 'Beautiful day in Portland!' 
        },
        { 
            'author': 'James',
            'date': 'December 27 2014', 
            'title': 'The Avengers movie was so cool!' 
        }
    ]
	return render_template('blog_base.html', posts = posts)


@app.route('/login', methods=['POST', 'GET'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		flash('Login requested for OpenID="%s", remember_me=%s'% 
			(form.openid.data, str(form.remember_me.data)))
		return redirect('/index')
	return render_template('login.html', title = 'Sign In', form = form)

@app.route('/index')
def index():
    pass


if __name__ == '__main__':

	app.debug = True
	app.run()

