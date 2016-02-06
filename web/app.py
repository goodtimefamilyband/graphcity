'''
app.py
'''

import urllib
from markupsafe import Markup
from flask import Flask, render_template, request, redirect
from flask.ext.mongoengine import MongoEngine
from flask.ext.mongoengine.wtf import model_form
from wtforms import PasswordField
from flask.ext.login import LoginManager, login_user, logout_user, login_required, current_user
import requests

app = Flask(__name__)

citylist = ["New York", "Chicago", "Philadelphia", "Paris", "Beijing", "Tokyo"]

@app.route("/")
def land():
	return render_template("land.html")

@app.route("/search", methods=["POST", "GET"])
def search():
	

'''
@app.after_request
def add_header(response):
	response.cache_control.max_age = 5
	return response
'''
		
if __name__ == "__main__":
	app.run(host="0.0.0.0")
	
