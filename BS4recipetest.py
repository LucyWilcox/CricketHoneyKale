from bs4 import BeautifulSoup as BS
import requests
import xml.etree.ElementTree
from pattern.web import plaintext
from recipedatabase import recipe_database
from string import find

class Recipe(object):
	def __init__(self, url):
		self.url = url

	def get_ingredient(self):
		r = requests.get(self.url)
		data = r.text	
		soup = BS(data)
		gross_ingredients = str(soup.find_all("li", {"itemprop":"ingredients"}))
		self.ingredients = str(plaintext(gross_ingredients).replace('\n', '').lower())


def create_recipes():
	recipes = []
	for url in recipe_database[:4]:
		recipes.append(Recipe(url))

create_recipes()

def find_one_ingredient(starter_ingredient, pure_ingredients):
	"""searches a list of ingredients + quantities for the given ingredient"""
	found = []
	for ingredient in pure_ingredients:
		found.append(ingredient.find(starter_ingredient))
	return found



# def grab_ingredients():
# 	"""Function that references recipedatabase.py in same folder to grab the html ingredients
# 	and return them as a list of strings"""
# 	ingredients = []
# 	for url in recipe_database[:4]:
# 		r = requests.get(url)
# 		data = r.text	
# 		soup = BS(data)

# 		ingredients.append(str(soup.find_all("li", {"itemprop":"ingredients"})))
# 	return ingredients

# def remove_tags(list_of_text):
# 	"""makes html tags prettier and gives us just the ingredients + quantities
# 	also a list of strings"""
# 	pure_ingredients= []
# 	for recipe in list_of_text:

# 		pure_ingredients.append(str(plaintext(recipe).replace('\n', '').lower()))
# 		#pure_ingredients.append(''.join(xml.etree.ElementTree.fromstring(recipe).itertext()))
# 	return pure_ingredients

def find_one_ingredient(starter_ingredient, pure_ingredients):
	"""searches a list of ingredients + quantities for the given ingredient"""
	found = []
	for ingredient in pure_ingredients:
		found.append(ingredient.find(starter_ingredient))
	return found


# html_disgusting = grab_ingredients()
# recipe_ingredients = remove_tags(html_disgusting)
# print find_one_ingredient('salt', recipe_ingredients)