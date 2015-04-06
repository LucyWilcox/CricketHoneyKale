from bs4 import BeautifulSoup as BS
import requests
from saladtoppings import *
from random import choice



def grab_ingredients():
	#htmls = ["AdonisCocktail.html", "bitchinapplecider.html"]
	url = "http://www.foodnetwork.com/recipes/food-network-kitchens/sausage-cauliflower-spaghetti-recipe.html"
	r = requests.get(url)
	data = r.text
	#print data
	results = []
	soup = BS(data)
	full_ingredients = str(soup.find_all("li"))
	print full_ingredients
 	groceries = soup.find_all("a", {"class": "ingr"})
 	return groceries


for i in range(0, 3):
	print choice(salad_ingredients)