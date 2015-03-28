from bs4 import BeautifulSoup as BS
htmls = ["AdonisCocktail.html", "bitchinapplecider.html"]
results = []
for site in htmls:
	soup = BS(open(site))
	results.append(soup.title)#find_all("li", {"class": "ingr"}))
print results