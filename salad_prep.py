from saladtoppings import *
from database_of_recipies import *
import nlkt
#import re


def raw_list():
	each_ingredient = []
	for recipe in recipes:
		seperated_ingredients = recipe.ingredients.replace(',', '').replace(']','').split("*")
		each_ingredient.extend(seperated_ingredients)
	each_ingredient = filter(lambda a: a != '[', each_ingredient)
	return each_ingredient

def next_thing(raw_list):
	print raw_list
	for i in raw_list:
		print i


raw_list = raw_list()
next_thing(raw_list)
salad_dict = dict.fromkeys(salad_ingredients)
print salad_dict