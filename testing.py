from saladtoppings import *
from random import choice
from limbo import *


#first_ingredient = choice(salad_ingredients)
current_ingredients = ['tomatoes']

class Salad(object):
	""" """
	def __init__(self, salad_ingredients):
		"""Sets first random topping"""
		self.toppings = ['tomatoes', 'salt']

	def add_ingredient(self, salad_ingredients):
		""" """
		possiblities = []
		for topping in self.toppings:
			for recipe in recipes:
				recipe.ingredient_used(topping)
				if recipe.ingredient_used == False:
					break
		possiblities.append(recipe.ingredients)

		possible_next_ingredient = []
		for recipe in possiblities:
			for ingredient in salad_ingredients:
				if ingredient in recipe:
					possible_next_ingredient.append(ingredient)
		next_ingredient = choice(possible_next_ingredient)
		self.toppings.append(next_ingredient)


salad1 = Salad(salad_ingredients)
salad1.add_ingredient(salad_ingredients)
print salad1.toppings

# def possible_next_options():
# 	possiblities = []
# 	for recipe in recipes:
# 		if recipe.ingredient_used == True:
# 			possiblities.append(recipe.ingredients)
# 	return possiblities

# def choose_next(recipes_remaining, dict_salad_ingredients):
# 	next_possiblities = []
# 	for recipe in recipes_remaining:
# 		for ingredient in dict_salad_ingredients.keys():
# 			if ingredient in recipe:
# 				next_possiblities.append(ingredient)
# 	return choice(next_possiblities)


# dict_salad_ingredients = dict.fromkeys(salad_ingredients)
# recipes_remaining = possible_next_options()
# print recipes_remaining


#print choose_next(first_ingredient, recipes_remaining, dict_salad_ingredients)



