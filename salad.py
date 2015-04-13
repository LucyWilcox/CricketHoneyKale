from saladtoppings import *
from random import choice
import pickle
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
		"""Adds a dressing if the salad is only vegtables, appends to toppings attribute"""
		for topping in self.toppings:
			if topping not in vegtables:
				return
		self.toppings.append(choice(dressing))

	def add_prep(self):
		with open('saladmethoddict.pickle', 'rb') as handle:
			b = pickle.load(handle)
		self.ingredients_string = ""
		for topping in self.toppings:
			if topping in b.keys():
				if b[topping] != None:
					self.ingredients_string += str(b[topping]) + " " + topping + ", "
				else:
					self.ingredients_string += " " + topping +  ", "
			else:
				self.ingredients_string += " " + topping +  ", "


def make_salad():
	""" """
	with open('themrecipies.pickle', 'rb') as handle:
		recipes = pickle.load(handle)


	salad1 = Salad(salad_ingredients, recipes)

	while len(salad1.toppings) < 4:
		salad1.get_remaining_recipies()
		salad1.add_ingredient(salad_ingredients)
		salad1.clear_recipies()

	salad1.dressing()
	salad1.add_prep()
	print salad1.toppings
	print salad1.ingredients_string


if __name__ == '__main__':
	make_salad()