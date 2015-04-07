from bs4 import BeautifulSoup as BS
import requests
import xml.etree.ElementTree
from pattern.web import plaintext
from recipedatabase import recipe_database
from string import find, split

class Recipe(object):
	""" """
	def __init__(self, url):
		"""Sets attributes of url and ingredient with amounts to each recipe"""
		self.url = url
		r = requests.get(self.url)
		data = r.text	
		soup = BS(data)
		gross_ingredients = str(soup.find_all("li", {"itemprop":"ingredients"}))
		self.ingredients = str(plaintext(gross_ingredients).replace('\n', '').lower())

	def ingredient_used(self, ingredient):
		""" If the ingredient is used in a recipe an attribuet ingredient_used is 
		set to True, else False """
		if ingredient in self.ingredients:
			self.ingredient_used = True
		else:
			self.ingredient_used = False
		#return self.ingredient_used

def create_recipe_database():
	recipes = []
	for url in recipe_database[:50]:
		recipes.append(Recipe(url))
	return recipes

def recipies_using_ingredient(recipes, ingredient):
	for recipe in recipes:
		recipe.ingredient_used(ingredient)


recipes = create_recipe_database() #each recipe is an object with attributes
#print recipes[1].ingredients

print recipes[1].ingredient_used('yellow squash') #okay so here I am running ingredient_used on recipe 1 and checking if it has yellow squash in it
#print recipes[1].ingredient_used #it does 

def txt_to_dict(txt):
    """Takes a txt file and breakes each new line into an entry of a dictionary
    """
    with open(txt) as f:
    	content = f.readlines()
    for i in range(len(content)):
    	content[i] = content[i].replace('\n', '').lower()
    d_content = dict.fromkeys(content)
    return d_content

food_list = txt_to_dict('foodlist.txt')
#print food_list

#recipies_using_ingredient(recipes, 'salt')

# for recipe in recipes:
# 	if recipe.ingredient_used == True:
# 		print True
# 	else:
# 		print False


# def find_one_ingredient(starter_ingredient, pure_ingredients):
# 	"""searches a list of ingredients + quantities for the given ingredient"""
# 	found = []
# 	for ingredient in pure_ingredients:
# 		found.append(ingredient.find(starter_ingredient))
# 	return found



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


# html_disgusting = grab_ingredients()
# recipe_ingredients = remove_tags(html_disgusting)
# print find_one_ingredient('salt', recipe_ingredients)