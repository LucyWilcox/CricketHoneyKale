from smoothies import *
#the other file containing smoothie ingredients in a list
from random import choice

class Smoothie(object):
	def __init__(self):
		self.create_random_smoothie(4)
		#runs the method below, which modifies the 
		#self.ingredient

	def __str__(self):
		#when you run this program, the class executes
		#and prints this string automatically
		return "This smoothie includes %s" %(self.ingredients)

	def create_random_smoothie(self,num_ingredients):
		#create a list of ingredients making a random smoothie
		self.ingredients = []
		#because I rebuild the ingredients every time I run this program, 
		#I want to not have self.ingredients set in the init but in the 
		#the create_random_smoothie, although it is referenced in the 
		#init
		for i in range(num_ingredients):
			self.ingredients.append(choice(smoothie_ingredients))
			#modifies self.ingredients to include new ingredients

peaches = Smoothie()
print peaches
