from bs4 import BeautifulSoup as BS


def grab_ingredients():
	htmls = ["AdonisCocktail.html", "bitchinapplecider.html"]
	results = []
	for site in htmls:
 		soup = BS(open(site))
 		full_ingredients = str(soup.find_all("li"))
 		groceries = soup.find_all("a", {"class": "ingr"})
	return groceries
print grab_ingredients()