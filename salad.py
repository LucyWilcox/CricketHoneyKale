from saladtoppings import *
from random import choice, randint
import pickle
from database_of_recipies import *
import re
from smoothies import *


class RandomRecipe(object):
	""" """
	def __init__(self, ingredients, recipes, recipe_type):
		"""Sets first random topping as attribute 
		also sets remaining_recipies_object as all recipes to begin with"""
		self.recipe_type = recipe_type
		self.toppings = [choice(ingredients)]
		print self.toppings
		self.ingredients = ingredients
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

		for recipe in self.remaining_recipies_object:
			possiblities.append(recipe.ingredients)
		self.remaining_recipies = possiblities # list of strs containing recipe.ingredients

	def clear_recipies(self):
		"""Clears remaining_recipies so they do not accumulate """
		self.remaining_recipies = []

	def add_ingredient(self):
		"""Adds ingredient to salad toppings attribute """
		possible_next_ingredient = []
		for recipe in self.remaining_recipies:
			for ingredient in self.ingredients:
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
					self.ingredients_string += str(choice(b[topping])) + " " + topping + ", "
				else:
					self.ingredients_string += " " + topping +  ", "
			else:
				self.ingredients_string += " " + topping +  ", "
		self.ingredients_string = self.ingredients_string[:-2]

	def add_instructions(self):
		if self.recipe_type == 'salad':
			self.instruction_string = "On top of a lush bed of greens, add: " + self.ingredients_string
		if self.recipe_type == 'smoothie':
			to_string = ', '.join(self.toppings)
			self.instruction_string = "Blend: " + to_string +  " and enjoy!"


def make_recipe(recipe_type):
	""" """
	with open('themrecipies.pickle', 'rb') as handle:
		recipes = pickle.load(handle)
	number_toppings = randint(3,6)

	if recipe_type == 'salad':
		salad1 = RandomRecipe(salad_ingredients, recipes, recipe_type)

		while len(salad1.toppings) < number_toppings:
			salad1.get_remaining_recipies()
			salad1.add_ingredient()
			salad1.clear_recipies()

		salad1.dressing()
		salad1.add_prep()
		salad1.add_instructions()
		#print salad1.ingredients_string
		print salad1.instruction_string

	if recipe_type == 'smoothie':
		smoothie1 = RandomRecipe(smoothie_ingredients, recipes, recipe_type)
		while len(smoothie1.toppings) < number_toppings:
			smoothie1.get_remaining_recipies()
			smoothie1.add_ingredient()
			smoothie1.clear_recipies()

		#smoothie1.add_instructions()
		print smoothie1.toppings
		print smoothie1.instruction_string

if __name__ == '__main__':
	#recipe_type = 'smoothie'
	recipe_type = 'salad'
	make_recipe(recipe_type)