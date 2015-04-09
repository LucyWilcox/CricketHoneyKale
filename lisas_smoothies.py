from smoothies import *
#the other file containing smoothie ingredients in a list
from random import choice
from database_of_recipies import *

class Smoothie(object):

	def __init__(self, smoothie_ingredients, recipes):
		"""Sets first random topping as attribute""" 
		"""also sets remaining_recipies_object as all recipes to begin with"""
		self.blending = [choice(smoothie_ingredients)]
		print self.blending
		self.remaining_recipies_object = recipes

	def __str__(self):
		#when you run this program, the class executes
		#and prints this string automatically
		return "This smoothie includes %s" %(self.blending)
	def get_remaining_recipies(self):
		"""Gets list of recipes that have the current toppings and sets as attribute
		also removes remaining_recipies_object that no longer contain all of the ingredients
		"""
		possiblities = []
		for blending in self.blending:
			for recipe in self.remaining_recipies_object:
				if blending not in recipe.ingredients:
					self.remaining_recipies_object.remove(recipe)
				elif recipe.ingredients not in possiblities:
					print "Not in"
					possiblities.append(recipe.ingredients)
				elif recipe.ingredients in possiblities:
					print "IN"
		self.remaining_recipies = possiblities

	def clear_recipies(self):
		"""Clears remaining_recipies so they do not accumulate """
		self.remaining_recipies = []

	def add_ingredient(self, smoothie_ingredients):
		"""Adds ingredient to smoothie blending attribute """
		possible_next_ingredient = []
		for recipe in self.remaining_recipies:
			for ingredient in smoothie_ingredients:
				if ingredient in recipe:
					possible_next_ingredient.append(ingredient)
		next_ingredient = choice(possible_next_ingredient)
		self.blending.append(next_ingredient)

def create_random_smoothie():
		#create a list of ingredients making a random smoothie
	#self.ingredients = []
		#because I rebuild the ingredients every time I run this program, 
		#I want to not have self.ingredients set in the init but in the 
		#the create_random_smoothie, although it is referenced in the 
		#init
	# 	for i in range(num_ingredients):
	# 		self.ingredients.append(choice(smoothie_ingredients))
	# 		#modifies self.ingredients to include new ingredients
	smoothie1 = Smoothie(smoothie_ingredients, recipes)
	for i in range(0,3):
		smoothie1.get_remaining_recipies()
		smoothie1.add_ingredient(smoothie_ingredients)
		smoothie1.clear_recipies()


	print smoothie1.blending

if __name__ == '__main__':
	create_random_smoothie()