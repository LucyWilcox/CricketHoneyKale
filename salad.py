from saladtoppings import salad_ingredients, dressing, vegtables
from soupingredientsstandard import soup_ingredients, base
from random import choice, randint
import pickle
from database_of_recipies import Recipe
import re
from smoothies import smoothie_ingredients
from dangerfactor import *


class RandomRecipe(object):
	"""Creates a generated recipe. Either a salad, soup or smoothie."""
	def __init__(self, ingredient_options, recipes, recipe_type, danger = 0):
		"""Sets first random topping as attribute 
		also sets remaining_recipies_object as all recipes to begin with"""
		self.recipe_type = recipe_type
		self.toppings = [choice(ingredient_options)]
		self.ingredient_options = ingredient_options
		self.remaining_recipies_object = recipes
		self.error = False
		self.danger = danger

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
			for ingredient in self.ingredient_options:
				if ingredient in recipe:
					if ingredient not in self.toppings:
						possible_next_ingredient.append(ingredient)

		if len(possible_next_ingredient) != 0:
			next_ingredient = choice(possible_next_ingredient)
			self.toppings.append(next_ingredient)
		else:
			self.error = True

	def adjust_danger(self):
		self.toppings = remix_to_danger(self)


	def dressing(self):
		"""Adds a dressing if the salad is only vegtables, appends to toppings attribute"""
		for topping in self.toppings:
			if topping not in vegtables:
				return
		self.toppings.append(choice(dressing))

	def add_soup_base(self):
		"""This method makes sure that soups have a base and if not it adds one randomly by appending it to toppings"""
		for topping in self.toppings:
			if topping in base:
				return
		self.toppings.append(choice(base))

	def add_prep(self):
		"""Adds prep methods via a pickled dictionary, it has some element of randomness as each ingredient has two different
		prep methods associated with it (if there are two, or any associated) there is a 2/3 chance the most common one will be chosen
		and a 1/3 chance the second most common one will be pickled.
		This method also converts the list of ingredients self.toppings into a string, self.ingredients_string
		"""
		with open('methoddict.pickle', 'rb') as handle:
			prep = pickle.load(handle)
		with open('amountdict.pickle', 'rb') as handle:
			amount = pickle.load(handle)

		if self.recipe_type == 'salad':
			self.ingredients_string = ""
			for topping in self.toppings:
				if topping in prep.keys():
					if prep[topping] != None:
						self.ingredients_string += str(choice(prep[topping])) + " " + topping + ", "
					else:
						self.ingredients_string += " " + topping +  ", "
				else:
					self.ingredients_string += " " + topping +  ", "

		elif self.recipe_type == 'soup':
			self.ingredients_string = ""
			for topping in self.toppings:
				if topping in prep.keys():
					if prep[topping] != None:
						self.ingredients_string += str(choice(amount[topping])) + str(choice(prep[topping])) + " " + topping + ", "
					else:
						self.ingredients_string += " " + topping +  ", "
				else:
					self.ingredients_string += " " + topping +  ", "				

		self.ingredients_string = self.ingredients_string[:-2]


	def add_instructions(self):
		"""Adds 'cookie cutter' style instructions which are revlevent depending the type of recipe being generated
		 """
		if self.recipe_type == 'salad':
			self.instruction_string = "On top of a lush bed of greens, add: " + self.ingredients_string
		if self.recipe_type == 'smoothie':
			to_string = ', '.join(self.toppings)
			self.instruction_string = "Blend: " + to_string +  " and enjoy!"
		if self.recipe_type == 'soup':
			self.instruction_string = "Put: " + self. ingredients_string + " in a crock pot or in a pot on the stovetop and heat till done!"


def make_recipe(recipe_type):
	"""Gerenates recipe with relevant method calls on the RandomRecipe class depending on the type of recipe """
	with open('themrecipies.pickle', 'rb') as handle:
		recipes = pickle.load(handle)
	number_toppings = randint(3,6)

	def run_cycle(recipe_name, number_toppings):
		while len(recipe_name.toppings) < number_toppings and recipe_name.error == False:
			recipe_name.get_remaining_recipies()
			recipe_name.add_ingredient()
			recipe_name.clear_recipies()

		if recipe_name.recipe_type == 'soup':
			recipe_name.add_soup_base()
			recipe_name.adjust_danger()
			recipe_name.add_prep()
			recipe_name.add_instructions()
			
			return recipe_name.instruction_string
		elif recipe_type == 'salad':
			recipe_name.dressing()
			recipe_name.adjust_danger()
			recipe_name.add_prep()
			recipe_name.add_instructions()
			return recipe_name.instruction_string
		elif recipe_type == 'smoothie':
			recipe_name.adjust_danger()
			recipe_name.add_instructions()
		 	return recipe_name.instruction_string

	if recipe_type == 'soup':
		created_recipe = RandomRecipe(soup_ingredients, recipes, recipe_type, 4)
	elif recipe_type == 'salad':
		created_recipe = RandomRecipe(salad_ingredients, recipes, recipe_type,4)
	elif recipe_type == 'smoothie':
		created_recipe = RandomRecipe(smoothie_ingredients, recipes, recipe_type, 5)

	return run_cycle(created_recipe, number_toppings)

if __name__ == '__main__':
	recipe_type = 'smoothie'
	#recipe_type = 'salad'
	#recipe_type = 'soup'
	instructions = make_recipe(recipe_type)
	print instructions