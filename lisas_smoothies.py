from smoothies import *
from random import choice

class Smoothie(object):
	def __init__(self):
		self.create_random_smoothie(4)
#		self.ingredients = ingredients

	def __str__(self):
		return "This smoothie includes %s" %(self.ingredients)

	def create_random_smoothie(self,num_ingredients):
		self.ingredients = []
		for i in range(num_ingredients):
			self.ingredients.append(choice(smoothie_ingredients))

peaches = Smoothie()
print peaches