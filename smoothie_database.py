smoothie_urls = ['http://www.foodnetwork.com/recipes/food-network-kitchens/green-smoothie.html',
'http://www.foodnetwork.com/recipes/food-network-kitchens/red-berry-and-beet-smoothie.html',
'http://www.foodnetwork.com/recipes/food-network-kitchens/carrot-pineapple-smoothie.html',
'http://www.foodnetwork.com/recipes/food-network-kitchens/strawberry-green-tea-smoothie.html',
'http://www.foodnetwork.com/recipes/food-network-kitchens/mango-coconut-and-chia-smoothie.html',
'http://www.foodnetwork.com/recipes/food-network-kitchens/peachy-oat-smoothie.html',
'http://www.foodnetwork.com/recipes/food-network-kitchens/blueberry-almond-smoothie.html',
'http://www.foodnetwork.com/recipes/food-network-kitchens/watermelon-and-cucumber-smoothie.html',
'http://www.foodnetwork.com/recipes/food-network-kitchens/apple-nut-smoothie.html',
'http://www.foodnetwork.com/recipes/food-network-kitchens/pumpkin-ginger-smoothie.html',
'http://www.foodnetwork.com/recipes/food-network-kitchens/cran-sicle-smoothie.html',
'http://www.foodnetwork.com/recipes/food-network-kitchens/banana-nog-smoothie.html',
'http://www.foodnetwork.com/recipes/sandra-lee/honeydew-smoothie-recipe.html',
'http://www.foodnetwork.com/recipes/anne-burrell/mango-strawberry-and-pineapple-smoothie-recipe.html',
'http://www.foodnetwork.com/recipes/ina-garten/tropical-smoothie-recipe.html',
'http://www.foodnetwork.com/recipes/ina-garten/orange-banana-smoothie-recipe.html',
'http://www.foodnetwork.com/recipes/bobby-flay/papaya-banana-smoothie-recipe.html',
'http://www.foodnetwork.com/recipes/giada-de-laurentiis/raspberry-vanilla-smoothie-recipe.html',
'http://www.foodnetwork.com/recipes/ellie-krieger/peach-pie-smoothie-recipe.html',
'http://www.foodnetwork.com/recipes/michael-chiarello/fresh-fruit-smoothie-recipe.html',
'http://www.foodnetwork.com/recipes/ina-garten/sunrise-smoothie-recipe.html',
'http://www.foodnetwork.com/recipes/jeff-mauro/power-smoothie.html',
'http://www.foodnetwork.com/recipes/melissa-darabian/green-morning-smoothie-recipe.html',
'http://www.foodnetwork.com/recipes/ina-garten/banana-raspberry-smoothies-recipe.html',
'http://www.foodnetwork.com/recipes/paula-deen/pina-colada-smoothie-recipe.html']
from bs4 import BeautifulSoup as BS
import requests
from smoothies import *
import xml.etree.ElementTree
from pattern.web import plaintext
smooth_ingredients = []
smooth_dict = {}
for url in smoothie_urls:
	r = requests.get(url)
	data = r.text	
	soup = BS(data)
	gross_ingredients = str(soup.find_all("li", {"itemprop":"ingredients"}))
	ingredients = str(plaintext(gross_ingredients).replace('\n', '').lower())
	for word in ingredients.split():
		if '[' or ']' or '/' or '*' or ',' or '.'in word:
			text = word.replace(']', '').replace('*', '').replace('(', '').replace(')', '').replace('/', '').replace('[', '').replace(',', '').replace('.', '')
			if text not in extra_units:
				if text not in methods:
					if text.isdigit() == False:
					#still need to filter: '2-inch' etc, 'one'-- the stupidly written out measurements
						smooth_ingredients.append(text)
print smooth_ingredients
for ingredient in smooth_ingredients:
	if ingredient in smooth_dict:
		val = smooth_dict.get(ingredient)
		val +=1
		smooth_dict[ingredient] = val
	else:
		smooth_dict[ingredient] = 1
print smooth_dict
			#smooth_ingredients.append(word)
	#smooth_ingredients.append(ingredients)
	#print ingredients
# from os.path import existss
# from bs4 import BeautifulSoup as BS
# import requests
# import pickle
# from pattern.web import plaintext
# filename = 'smoothie_database.txt'

# ingredient_list = []
# for recipe_url in smoothie_urls:
# 	fi = open(filename, 'rw')
# 	ingredient_list = [pickle.load(fi)]
# 	r = requests.get(recipe_url)
# 	data = r.text
# 	soup = BS(data)
# 	gross_ingredients = str(soup.find_all("li", {"itemprop":"ingredients"}))
# 	ingredients = str(plaintext(gross_ingredients).replace('\n', '').lower())
# 	ingredient_list.append(ingredients)
# 	pickle.dump(ingredient_list, open('smoothie_database.txt', 'w'))
# fi.close()

# for smoothie in smoothie_urls:
# 	print>>'smoothie_database.txt', smoothie_urls