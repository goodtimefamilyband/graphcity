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
app.config["DEBUG"] = True

app.config['MONGODB_SETTINGS'] = { 'db' : 'graphcity' }
db = MongoEngine(app)

class CityNode(db.Document):
	name = db.StringField(required=True, unique=True)

class CityLink(db.Document):
	source = db.ReferenceField(CityLink)
	target = db.ReferenceField(CityLink)
	weight = db.FloatField(required=True)

@app.route("/")
def land():
	return render_template("land.html")

@app.route("/search", methods=["POST", "GET"])
def search():
	citycount = 5
	if request.method == "POST":
		countries = CountryLink.
	
	return render_template("search.html", citycount=citycount, msg="foo");

'''
@app.after_request
def add_header(response):
	response.cache_control.max_age = 5
	return response
'''
		
if __name__ == "__main__":
	app.run(host="0.0.0.0")
	
