##main file of Cricket Honey Kale Recipe Generation###
from saladtoppings import salad_ingredients, dressing, vegtables
from soupingredientsstandard import soup_ingredients, base
from random import choice, randint
import pickle
from database_of_recipies import Recipe
from sandwich_ingredients import sandwich_ingredients
from smoothies import smoothie_ingredients
from dangerfactor import remix_to_danger
from  string import strip

class RandomRecipe(object):
	"""Creates a generated recipe. Either a salad, sandwich, soup or smoothie."""
	def __init__(self, ingredient_options, recipes, recipe_type, allergen, danger = 0):
		"""Sets first random topping as attribute 
		also sets remaining_recipies_object as all recipes to begin with
		error is False, gets set as True as needed
		danger is set by user input, or set as 0 if nothing is entered
		ingredient_options depends on the type of recipe and is passed in"""
		self.recipe_type = recipe_type
		self.toppings = [choice(ingredient_options)]
		self.ingredient_options = ingredient_options
		self.remaining_recipies_object = recipes
		self.error = False
		self.danger = danger
		self.allergen = allergen

	def get_remaining_recipies(self):
		"""Gets list of recipes that have the current toppings and sets as attribute
		also removes remaining_recipies_object that no longer contain all of the ingredients
		"""
		possiblities = []
		for topping in self.toppings: #loops through current toppings
			for recipe in self.remaining_recipies_object: #and Recipe objects
				if topping not in recipe.ingredients: # if the topping is not in the recipe...
					self.remaining_recipies_object.remove(recipe) #then the recipe is not relavent and can be deleted

		for recipe in self.remaining_recipies_object: #if the recipe is still relvant...
			possiblities.append(recipe.ingredients) #add the ingredients it contains to a list
		self.remaining_recipies = possiblities # list of strs containing recipe.ingredients

	def clear_recipies(self):
		"""Clears remaining_recipies so they do not accumulate """
		self.remaining_recipies = []

	def add_ingredient(self):
		"""Adds ingredient to salad toppings attribute """
		possible_next_ingredient = []
		for recipe in self.remaining_recipies: # loops through each recipe left
			for ingredient in self.ingredient_options: #and each possible ingredient for the food type
				if ingredient in recipe: #if the ingredient is in the recipe...
					if ingredient not in self.toppings: #and not in the current toppings...
						possible_next_ingredient.append(ingredient) #add it to the list of toppings to choose from
		if len(possible_next_ingredient) != 0:
			next_ingredient = choice(possible_next_ingredient) #choose a random ingredient from the list
			while next_ingredient in self.allergen: #if it is a listed allergy chose again
				next_ingredient = choice(possible_next_ingredient)
			self.toppings.append(next_ingredient) #appened it to the current toppings
		else:
			self.error = True #error means that there are no more viable ingeredients and even if the generated number of ingredient has not been met
									#its time to stop the recipe where it is

	def adjust_danger(self):
		"""Runs the correct danger level in dangerfactor file and relaces topping """
		self.toppings = remix_to_danger(self) #remix to danger in a function in dangerfactor.py

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

		if self.recipe_type in ['salad', 'sandwich']: #adds preperation method
			self.ingredients_string = ""
			for topping in self.toppings:
				if topping in prep.keys():
					if prep[topping] != None:
						self.ingredients_string += str(choice(prep[topping])) + " " + topping + ", "
					else:
						self.ingredients_string += " " + topping +  ", "
				else:
					self.ingredients_string += " " + topping +  ", "

		elif self.recipe_type == 'soup': #adds preperation method and amounts
			self.ingredients_string = ""
			for topping in self.toppings:
				if topping in prep.keys():
					if prep[topping] != None:
						self.ingredients_string += str(choice(amount[topping])) + str(choice(prep[topping])) + " " + topping + ", "
					else:
						self.ingredients_string += " " + topping +  ", "
				else:
					self.ingredients_string += " " + topping +  ", "	

		self.ingredients_string = self.ingredients_string[:-2] #-2 takes of the last un-needed ", "

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
		if self.recipe_type == 'sandwich':
			self.instruction_string  = "Put: " + self.ingredients_string + " between two slices of your favorite bread (or whatever crap you have) and chow down."


def make_recipe(recipe_type,  allergen, danger_level = 0):
	"""Gerenates recipe with relevant method calls on the RandomRecipe class depending on the type of recipe """
	with open('themrecipies.pickle', 'rb') as handle:
		recipes = pickle.load(handle)
	number_toppings = randint(3,6)

	allergen = allergen.split(",")
	allergen = [strip(entry) for entry in allergen]

	def run_cycle(recipe_name, number_toppings, allergen):
		"""Runs through the code by changing attributes on recipe then calling certian methods for
		for different recipe types
		"""
		while len(recipe_name.toppings) < number_toppings and recipe_name.error == False:
			recipe_name.get_remaining_recipies()
			recipe_name.add_ingredient()
			recipe_name.clear_recipies()

		for topping in recipe_name.toppings:
			if topping in allergen:
				recipe_name.toppings.remove(topping)

		recipe_name.adjust_danger()

		if recipe_name.recipe_type == 'soup':
			recipe_name.add_soup_base()
			recipe_name.add_prep()
			recipe_name.add_instructions()
			return recipe_name.instruction_string

		elif recipe_type == 'salad':
			recipe_name.dressing()
			recipe_name.add_prep()
			recipe_name.add_instructions()
			return recipe_name.instruction_string

		elif recipe_type == 'smoothie':
			recipe_name.add_instructions()
		 	return recipe_name.instruction_string

		elif recipe_type == 'sandwich':
			recipe_name.add_prep()
			recipe_name.add_instructions()
			return recipe_name.instruction_string

	if recipe_type == 'soup':
		created_recipe = RandomRecipe(soup_ingredients, recipes, recipe_type, allergen, danger_level)
	elif recipe_type == 'salad':
		created_recipe = RandomRecipe(salad_ingredients, recipes, recipe_type, allergen, danger_level)
	elif recipe_type == 'smoothie':
		created_recipe = RandomRecipe(smoothie_ingredients, recipes, recipe_type, allergen, danger_level)
	elif recipe_type == 'sandwich':
		created_recipe = RandomRecipe(sandwich_ingredients, recipes, recipe_type, allergen, danger_level)

	return run_cycle(created_recipe, number_toppings, allergen)

if __name__ == '__main__':
	"""You can test main from here. Uncomment prefered recipe type and change alergen and danger level
	as desired"""
	#recipe_type = 'smoothie'
	#recipe_type = 'salad'
	recipe_type = 'soup'
	#recipe_type = 'sandwich'
	instructions = make_recipe(recipe_type, allergen = 'milk, sugar, ice', danger_level = 0)
	print instructions