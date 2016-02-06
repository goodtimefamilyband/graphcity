from pymongo import MongoClient
import logging
import sys
import os
from os.path import join
from genericpath import isfile
import json
from bson.json_util import dumps
from bson import json_util, ObjectId
import traceback
import ijson
from mongoengine import *

connect("graphcity")

class City(Document):
	name = StringField(required=True)
	
class CityLink(Document):
	source = ReferenceField(City)
	target = ReferenceField(City)
	weight = StringField(required=True)

print 'Reading JSON...'

try:
	path = 'dist.json'
	filehandle = open(path, 'r')
	json_obj = ijson.items(filehandle, '').next()
	
	cityDict = dict()
	
	
	for key, value in json_obj.items():
		city = City(name=key)
		city.save()
		
	filehandle.close()
	filehandle = open(path, 'r')
	json_obj = ijson.items(filehandle, '').next()
	for city, links in json_obj.items():
		for link in links:
			citysrc = City.objects(name=city).first()
			citydst = City.objects(name=link).first()
			strweight = str(links[link])
			citylink = CityLink(source=citysrc, target=citydst, weight=strweight)
			citylink.save()
			
	
		
except Exception as e:
    traceback.print_exc()
	