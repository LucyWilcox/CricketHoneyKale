from bs4 import BeautifulSoup as BS
import requests


def grab_ingredients():
	#htmls = ["AdonisCocktail.html", "bitchinapplecider.html"]
	url = "http://www.drinknation.com/drink/mai-tai"
	r = requests.get(url)
	data = r.text
	print data
	results = []
	soup = BS(data)
	full_ingredients = str(soup.find_all("li"))
 	groceries = soup.find_all("a", {"class": "ingr"})
 	return groceries



print grab_ingredients()
