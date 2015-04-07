import random
from soupingredients import base
from soupingredients import fats
from soupingredients import starch
from soupingredients import meat
from soupingredients import spices
from soupingredients import vegetables
from soupingredients import legumes
from soupingredients import toppings

def makesoup():
	
	def choosebase():
		num = random.randint(0,len(base)-1)
		if type (base[num]) == str:
			baseingredient = base[num]
			#print "not a list"
		elif type (base[num]) == list :
			baseingredient = base[num][random.randint(0,len(base[num])-1)] 
			#print "its a list"
		return baseingredient

	def choosefat():
		num = random.randint(0,len(fats)-1)
		if type (fats[num]) == str:
			fatingredient = fats[num]
			#print "not a list"
		elif type (fats[num]) == list :
			baseingredient = fats[num][random.randint(0,len(base[num])-1)] 
			#print "its a list"
		return fatingredient

	def choosestarch():
		num = random.randint(0,len(starch)-1)
		if type (starch[num]) == str:
			starchingredient = starch[num]
			#print "not a list"
		elif type (starch[num]) == list :
			starchingredient = starch[num][random.randint(0,len(starch[num])-1)] 
			#print "its a list"
		return starchingredient

	def choosemeat():
		num = random.randint(1,5)
		if num < 5:    ###  Later change this section to make it vegetarian if the user says to
			num = random.randint(0,len(meat)-1)
			if type (meat[num]) == str:
				meatingredient = meat[num]
			elif type (meat[num]) == list :
				meatingredient = meat[num][random.randint(0,len(meat[num])-1)] 
			if type(meatingredient) == str :
				return meatingredient
				#### to do: make sure the 


	def choosespices():
		num = random.randint(1,5)
		if num < 5:    ###  Later change this section to make it vegetarian if the user says to
			num = random.randint(0,len(starch)-1)
			if type (starch[num]) == str:
				starchingredient = starch[num]
			elif type (starch[num]) == list :
				starchingredient = starch[num][random.randint(0,len(base[num])-1)] 
			return 

	print choosebase()
	print choosefat()
	print choosestarch()
	print choosemeat()
	# print choosespices()
	# print choosevegetables()
	# print chooselegumes()
	# print choosetoppings()

# print "instructions: " 
# print "In a heavy bottomed pot, cook " 
# print choosevegatables() 
# print " and "
# print choosemeat()
# print " in the " 
# print choosefat
# print "Add "
# print choosebase()
# print " and "
# print choosespices()
# print " and simmer for time." 
# print "Stir in "
# print choosestarch()
# print " and "
# print chooselegumes()
# print" and simmer for time. Serve in bowls with "
# print choosetopping() 


print makesoup()
