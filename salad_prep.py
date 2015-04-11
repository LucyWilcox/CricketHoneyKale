from saladtoppings import *
from database_of_recipies import *
import nltk
import re


def raw_list():
	each_ingredient = []
	for recipe in recipes:
		seperated_ingredients = recipe.ingredients.replace(',', '').replace(']','').split("*")
		each_ingredient.extend(seperated_ingredients)
	each_ingredient = filter(lambda a: a != '[', each_ingredient)
	return each_ingredient

def next_thing(raw_list):
	good_pos = ['RB', 'VBN']
	text = nltk.word_tokenize(raw_list)
	tags = nltk.pos_tag(text)
	good_types = []
	for tag in tags:
		tag
		if tag[1] in good_pos:
			good_types.append(tag[0])
	return good_types

def refine_tags(raw_list, salad_ingredients):
	salad_dict = dict.fromkeys(salad_ingredients)

	for method in raw_list:
		for key in salad_dict:
			if key in method:
				tags = next_thing(method)
				if salad_dict[key] == None:
					print next_thing(method)
					salad_dict[key] = [method]
				else:
					salad_dict[key].append(method)
	print salad_dict
	# for step in tags:
	# 	for (p1, p2) in step:
	# 		if p2 in good_pos:
	# 			print p1
	# 		else:
	# 			print 'nope', (p1, p2)
	# 			#del (p1,p2)
	# print refine

raw_list = raw_list()
#print raw_list
#tags = next_thing(raw_list)
refine_tags(raw_list, salad_ingredients)