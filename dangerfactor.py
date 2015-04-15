###REMIXX###
# Steps:
# 1. Call the inputted type of food twice or more
# 2. Identify the similarities (3 toppings, 1 dressing)
# 3. Pick 1 or more(depending on danger level) things to swap
# 4. OR/AND add a "danger ingredient list" and add a certain number of those to the recipe
from saladtoppings import *
from database_of_recipies import create_recipe_database
from random import choice, randint
import pickle
from database_of_recipies import *
import re
from smoothies import *
from salad import *
from salad import make_recipe


class Danger_Factor(object):
	def __init__(self, food_type, danger_level):
		self.food_type = food_type
		self.danger_level = danger_level

	def level_one(self, food_type):
		smoothie_1 = make_recipe(food_type)
		smoothie_2 = make_recipe(food_type)
		print smoothie_1
		print smoothie_2
		for i in range(len(smoothie_1)):
			for j in range(len(smoothie_2)):
				if smoothie_1[i] == smoothie_2[j]:
					smoothie_1[i] = choice(smoothie_2)
					smoothie_2[j] = choice(smoothie_1)
		return smoothie_1, smoothie_2

if __name__ == '__main__':
	First_level = Danger_Factor('smoothie', 1)
	print First_level.level_one('smoothie')