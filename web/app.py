'''
app.py
'''

import urllib
import json
import flask
from decimal import Decimal
from markupsafe import Markup
from flask import Flask, render_template, request, redirect
from flask.ext.mongoengine import MongoEngine
from flask.ext.mongoengine.wtf import model_form

import requests

app = Flask(__name__)
app.config["DEBUG"] = True

app.config['MONGODB_SETTINGS'] = { 'db' : 'graphcity' }
db = MongoEngine(app)

class City(db.Document):
	name = db.StringField(required=True)
	
class CityLink(db.Document):
	source = db.ReferenceField(City)
	target = db.ReferenceField(City)
	weight = db.StringField(required=True)
	
class CityData(db.Document):
	city = db.ReferenceField(City)
	country = db.StringField()
	population = db.IntField()
	area = db.FloatField()
	density = db.IntField()

@app.route("/")
def land():
	return render_template("land.html")

@app.route("/search", methods=["POST", "GET"])
def search():
	citycount = 5
	if request.method == "POST":
		city = City.objects(name=request.form["city1"]).first()
		if(city is None):
			return render_template("/land.html", msg="City not found :(");
		return render_template("search.html", cityname=request.form["city1"]);
		
	return render_template("search.html")
	
@app.route("/cityinfo/<cityname>")
def cityinfo(cityname):
	city = City.objects(name=cityname).first()
	citylinks = CityLink.objects(source=city).order_by('-weight').limit(5)
	
	cityDict = {}
	cityDict['nodes'] = [{"name":cityname, "group": 0, "cityweight":1}]
	cityDict['links'] = []
	
	i = 1
	for citylink in citylinks:
		cityDict['nodes'].append({"name":citylink.target.name,"group":1,"cityweight":float(citylink.weight)})
		cityDict['links'].append({"source":i, "target":0, "value":float(citylink.weight)})
		i = i + 1
		
	return flask.jsonify(**cityDict)
	
@app.route("/details/<source>/<target>")
def details(source, target):
	citysource = City.objects(name=source).first()
	citytarget = City.objects(name=target).first()
	
	cdsource = CityData.objects(city=citysource).first()
	cdtarget = CityData.objects(city=citytarget).first()
	
	return render_template("details.html", source=cdsource, target=cdtarget)
	
@app.route("/citydata/<source>/<target>")
def citydata(source, target):
	citysource = City.objects(name=source).first()
	citytarget = City.objects(name=target).first()
	
	cdsource = CityData.objects(city=citysource).first()
	cdtarget = CityData.objects(city=citytarget).first()

	dataDict = {}
	
	dataDict["source"] = {"city":citysource.name, "country":cdsource.country, "population":cdsource.population, "area":cdsource.area, "density":cdsource.density}
	dataDict["target"] = {"city":citytarget.name, "country":cdtarget.country, "population":cdtarget.population, "area":cdtarget.area, "density":cdtarget.density}
	
	return flask.jsonify(**dataDict)
	

'''
@app.after_request
def add_header(response):
	response.cache_control.max_age = 5
	return response
'''
		
if __name__ == "__main__":
	app.run(host="0.0.0.0")
	
