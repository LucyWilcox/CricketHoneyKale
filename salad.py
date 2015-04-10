from saladtoppings import *
from random import choice
from database_of_recipies import *


class Salad(object):
	""" """
	def __init__(self, salad_ingredients, recipes):
		"""Sets first random topping as attribute 
		also sets remaining_recipies_object as all recipes to begin with"""
		self.toppings = [choice(salad_ingredients)]
		print self.toppings
		#self.toppings = ['tomato']
		self.remaining_recipies_object = recipes

	def get_remaining_recipies(self):
		"""Gets list of recipes that have the current toppings and sets as attribute
		also removes remaining_recipies_object that no longer contain all of the ingredients
		"""
		possiblities = []
		for topping in self.toppings:
			for recipe in self.remaining_recipies_object:
				if topping not in recipe.ingredients:
					self.remaining_recipies_object.remove(recipe)
				else:
					possiblities.append(recipe.ingredients)
		self.remaining_recipies = possiblities # list of strs containing recipe.ingredients

	def clear_recipies(self):
		"""Clears remaining_recipies so they do not accumulate """
		self.remaining_recipies = []

	def add_ingredient(self, salad_ingredients):
		"""Adds ingredient to salad toppings attribute """
		possible_next_ingredient = []
		for recipe in self.remaining_recipies:
			for ingredient in salad_ingredients:
				if ingredient in recipe:
					possible_next_ingredient.append(ingredient)
		next_ingredient = choice(possible_next_ingredient)
		if next_ingredient not in self.toppings:
			self.toppings.append(next_ingredient)

	def dressing(self):
		if all(topping in self.toppings in vegtables):
			self.toppings.append(choice(dressing))


def make_salad():
	""" """
	#recipes = open('recipe_data.pk1', 'rb')
	#print type(recipes)
	salad1 = Salad(salad_ingredients, recipes)
	while len(salad1.toppings) < 4:
		salad1.get_remaining_recipies()
		salad1.add_ingredient(salad_ingredients)
		salad1.clear_recipies()

	print salad1.toppings

if __name__ == '__main__':
	make_salad()