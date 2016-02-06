import csv
from mongoengine import *

connect("graphcity")

class City(Document):
	name = StringField(required=True)

class CityData(Document):
	city = ReferenceField(City)
	country = StringField()
	population = IntField()
	area = FloatField()
	density = IntField()

with open('urbanareas.csv', 'r') as csvfile:
	reader = csv.DictReader(csvfile, delimiter=",")
	for row in reader:
		city = City.objects(name=row["City"]).first()
		country = row["Country"]
		population = int(row["Population"].replace(",",""))
		area = float(row["Area"].replace(",",""))
		density = int(row["Density"].replace(",",""))
		citydata = CityData(city=city, country=country, population=population, area=area, density=density)
		citydata.save()