from saladtoppings import *
from database_of_recipies import *
import nltk
import re
from collections import Counter
import pickle



def raw_list():
	each_ingredient = []
	for recipe in recipes:
		seperated_ingredients = recipe.ingredients.replace(',', '').replace(']','').split("*")
		each_ingredient.extend(seperated_ingredients)
	each_ingredient = filter(lambda a: a != '[', each_ingredient)
	return each_ingredient


def each_prep_methods(raw_list, salad_ingredients):
	good_pos = ['VBN']
	text = nltk.word_tokenize(raw_list)
	tags = nltk.pos_tag(text)
	good_types = []
	for tag in tags:
		if tag[1] in good_pos and tag[0] not in salad_ingredients:
			good_types.append(tag)
	return good_types


def full_method_dict(raw_list, salad_ingredients):
	salad_dict = dict.fromkeys(salad_ingredients)
	for method in raw_list:
		for key in salad_dict:
			if key in method:
				tags = each_prep_methods(method, salad_ingredients)
				if tags != []:
					if key == tags[0]:
						pass
					elif salad_dict[key] == None:
						salad_dict[key] = tags
					else:
						salad_dict[key].extend(tags)
	return salad_dict


def get_top_methods(long_dict):
	for key in long_dict:
		methods = long_dict[key]
		VBN = []
		if methods != None:
			for method in methods:

				VBN.append(method[0])
			cVBN = Counter(VBN)
			topVBN = [ite for ite, it in cVBN.most_common(1)]
			long_dict[key] = topVBN[0]
	return long_dict


def pickle_it(short_dict):
	with open('saladmethoddict.pickle', 'wb') as handle:
		pickle.dump(short_dict, handle)
	with open('saladmethoddict.piclke', 'rb') as handle:
		b = pickle.load(handle)

	print b

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
long_dict = full_method_dict(raw_list, salad_ingredients)
short_dict = get_top_methods(long_dict)
pickle_it(short_dict)
