#!/usr/bin/env python3
from flask.ext.login import LoginManager, UserMixin, login_user, logout_user, login_required
from flask.ext.sqlalchemy import SQLAlchemy
from flask import Flask, render_template, session, request, send_from_directory, request, abort, flash, redirect, url_for
import os

DEBUG = True
SECRET_KEY = 'memes'
SQLALCHEMY_DATABASE_URI = 'sqlite:///db/sql.db'
# SQLALCHEMY_TRACK_MODIFICATIONS = True

app = Flask(__name__)
app.secret_key = 'Bc9on)Dhb308rj98HER87g67rN*&^F767h^&*#HH(F3b987vbf9H#'

login_manager = LoginManager(app)
login_manager.init_app(app)
 
db = SQLAlchemy(app)
 
# Models

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    password = db.Column(db.String)

# Routes

@app.before_first_request
def init_request():
    db.create_all()

@app.route('/',methods=['GET','POST'])
@app.route('/index',methods=['GET','POST'])
def index():
	return render_template('index.html')

@app.route('/login',methods=['GET','POST'])
def login():
	if request.method == 'GET':
		return render_template('login.html', next=request.args.get('next'))
	elif request.method == 'POST':
		username = request.form['username']
		password = request.form['password']
		 
		user = User.query.filter_by(username=username)
		if user.count() == 0:
			user = User(username=username, password=password)
			db.session.add(user)
			db.session.commit()
		 
			flash('You have registered the username {0}. Please login'.format(username))
			return redirect(url_for('login'))
		else:
			flash('The username {0} is already in use.  Please try a new username.'.format(username))
			return redirect(url_for('register'))
	else:
		abort(405)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    elif request.method == 'POST':
        pass
    else:
        abort(405)

@app.route('/secret')
@login_required
def secret():
	return render_template('secret.html')

@app.route('/static/<path:path>')
def send_static():
	return send_from_directory('static',path) #needed for some files like FA

if __name__ == '__main__':
    app.run(debug=True) #start on localhost:5000,proxied through apache
