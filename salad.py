from saladtoppings import *
from random import choice
from limbo import *


#first_ingredient = choice(salad_ingredients)
current_ingredients= ['tomatoes']

class Salad(object):
	""" """
	def __init__(self, salad_ingredients):
		"""Sets first random topping"""
		self.toppings = ['cucumber']

	def add_ingredient(self, salad_ingredients):
		""" """
		possiblities = []
		for topping in self.toppings:
			for recipe in recipes:
				if topping not in recipe.ingredients:
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
for i in range(0,3):
	salad1.add_ingredient(salad_ingredients)
print salad1.toppings