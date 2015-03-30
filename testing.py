from bs4 import BeautifulSoup as BS
import requests


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



print grab_ingredients()
