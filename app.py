#!/usr/bin/env python3
from flask import Flask, render_template, session, request, send_from_directory
app = Flask(__name__)
app.secret_key = 'Bc9on)Dhb308rj98HER87g67rN*&^F767h^&*#HH(F3b987vbf9H#'

@app.route('/',methods=['GET','POST'])
def index():
	return render_template('index.html',name='James Houghton')
@app.route('/static/<path:path>')
def send_static():
	return send_from_directory('static',path) #needed for some files like FA

if __name__ == '__main__':
    app.run(debug=True) #start on localhost:5000,proxied through apache
