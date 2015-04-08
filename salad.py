from saladtoppings import *
from random import choice
from limbo import *


#first_ingredient = choice(salad_ingredients)

class Salad(object):
	""" """
	def __init__(self, salad_ingredients, recipes):
		"""Sets first random topping"""
		#self.toppings = choice(salad_ingredients)
		self.toppings = ['salmon']
		
	def get_remaining_recipies(self):
		"""Gets list of recipes that have the current toppings"""
		possiblities = []
		for topping in self.toppings:
			for recipe in recipes:
				if topping not in recipe.ingredients:
					pass
				else:
					possiblities.append(recipe.ingredients)
		self.remaining_recipies = possiblities

	def add_ingredient(self, salad_ingredients):
		""" """
		possible_next_ingredient = []
		for recipe in self.remaining_recipies:
			for ingredient in salad_ingredients:
				if ingredient in recipe:
					possible_next_ingredient.append(ingredient)
		next_ingredient = choice(possible_next_ingredient)
		self.toppings.append(next_ingredient)


salad1 = Salad(salad_ingredients, recipes)
for i in range(0,3):
	salad1.get_remaining_recipies()
	salad1.add_ingredient(salad_ingredients)



print salad1.toppings