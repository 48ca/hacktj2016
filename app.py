#!/usr/bin/env python3
from flask.ext.login import LoginManager, UserMixin, login_user, logout_user, login_required
from flask.ext.sqlalchemy import SQLAlchemy
from flask import Flask, render_template, session, request, send_from_directory, request, abort, flash, redirect, url_for
import os

from database import init_db

SQLALCHEMY_DATABASE_URI = "postgresql://cov:memes@localhost/covalence"

app = Flask(__name__)
app.secret_key = 'Bc9on)Dhb308rj98HER87g67rN*&^F767h^&*#HH(F3b987vbf9H#'
app.config.from_object('config')
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI

login_manager = LoginManager(app)
login_manager.init_app(app)

init_db() 

db = SQLAlchemy(app)

# Models

class User(db.Model, UserMixin):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String)
	password = db.Column(db.String)

	def __init__(self, username, password):
		self.username = username
		self.password = password
	def __repr__(self):
		return username

# Routes

@app.before_first_request
def init_request():
    db.create_all()

@app.route('/',methods=['GET','POST'])
@app.route('/index',methods=['GET','POST'])
def index():
	return redirect('/home')
	# return render_template('index.html')

@app.route('/register',methods=['GET','POST'])
def register():
	if request.method == 'GET':
		return render_template('register.html', next=request.args.get('next'))
	elif request.method == 'POST':
		username = request.form['username']
		password = request.form['password']
		 
		user = User.query.filter_by(username=username)
		if user.count() == 0:
			user = User(username=username, password=password)
			db.session.add(user)
			db.session.commit()

			# flash('You have registered the username {0}. Please login'.format(username))
			return redirect(url_for('login'))
			# return redirect(url_for('home'))
		else:
			flash('The username {0} is already in use.  Please try a new username.'.format(username))
			return redirect(url_for('register'))
	else:
		abort(405)

@app.route('/login',methods=['GET','POST'])
def login():
	if request.method == 'GET':
		return render_template('login.html', next=request.args.get('next'))
	elif request.method == 'POST':
		username = request.form['username']
		password = request.form['password']
		 
		user = User.query.filter_by(username=username).filter_by(password=password)
		if user.count() == 1:
			login(user.one())
			try:
				next = request.form['next']
				return redirect(url_for(next))
			except:
				return redirect(url_for('home'))
			# flash('You have registered the username {0}. Please login'.format(username))
			return redirect(url_for('home'))
		else:
			flash('Incorrect username and password combination: {} {}'.format(username,password))
			return redirect(url_for('login'))
	else:
		abort(405)


@app.route('/home')
# @login_required
def home():
	return render_template('home.html')

@app.route('/upload')
def upload()
	return render_template('upload.html')

@app.route('/static/<path:path>')
def send_static():
	return send_from_directory('static',path) #needed for some files like FA

if __name__ == '__main__':
    app.run(debug=True) #start on localhost:5000,proxied through apache
