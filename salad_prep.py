from saladtoppings import *
from database_of_recipies import *
import nltk
import re
from collections import Counter
import pickle


class PrepDict(object):

	def __init__(self, recipes, ingredients_used, file_name):
		self.recipes = recipes
		self.ingredients_used = ingredients_used
		self.file_name = file_name

	def get_raw_list(self):
		each_ingredient = []
		for recipe in self.recipes:
			seperated_ingredients = recipe.ingredients.replace(',', '').replace(']','').split("*")
			each_ingredient.extend(seperated_ingredients)
		each_ingredient = filter(lambda a: a != '[', each_ingredient)
		self.raw_list = each_ingredient

	def full_method_dict(self):
		def each_prep_methods(method, ingredients_used):
			good_pos = ['VBN']
			text = nltk.word_tokenize(method)
			tags = nltk.pos_tag(text)
			good_types = []
			for tag in tags:
				if tag[1] in good_pos and tag[0] not in ingredients_used:
					good_types.append(tag)
			return good_types

		method_dict = dict.fromkeys(self.ingredients_used)
		for method in self.raw_list:
			for key in method_dict:
				if key in method:
					tags = each_prep_methods(method, self.ingredients_used)
					if tags != []:
						if key == tags[0]:
							pass
						elif method_dict[key] == None:
							method_dict[key] = tags
						else:
							method_dict[key].extend(tags)
		self.long_dict = method_dict

	def get_top_methods(self):
		for key in self.long_dict:
			methods = self.long_dict[key]
			VBN = []
			if methods != None:
				for method in methods:

					VBN.append(method[0])
				cVBN = Counter(VBN)
				topVBN = [ite for ite, it in cVBN.most_common(1)]
				self.long_dict[key] = topVBN[0]
		#self.short_dict = long_dict


	def pickle_it(self):
		with open(self.file_name, 'wb') as handle:
			pickle.dump(self.long_dict, handle)


with open('themrecipies.pickle', 'rb') as handle:
	recipes = pickle.load(handle)
salad = PrepDict(recipes, salad_ingredients, 'saladmethoddict.pickle')
salad.get_raw_list()
salad.full_method_dict()
salad.get_top_methods()
salad.pickle_it()
print salad.long_dict


# def raw_list():
# 	each_ingredient = []
# 	for recipe in recipes:
# 		seperated_ingredients = recipe.ingredients.replace(',', '').replace(']','').split("*")
# 		each_ingredient.extend(seperated_ingredients)
# 	each_ingredient = filter(lambda a: a != '[', each_ingredient)
# 	return each_ingredient


# def each_prep_methods(raw_list, salad_ingredients):
# 	good_pos = ['VBN']
# 	text = nltk.word_tokenize(raw_list)
# 	tags = nltk.pos_tag(text)
# 	good_types = []
# 	for tag in tags:
# 		if tag[1] in good_pos and tag[0] not in salad_ingredients:
# 			good_types.append(tag)
# 	return good_types


# def full_method_dict(raw_list, salad_ingredients):
# 	salad_dict = dict.fromkeys(salad_ingredients)
# 	for method in raw_list:
# 		for key in salad_dict:
# 			if key in method:
# 				tags = each_prep_methods(method, salad_ingredients)
# 				if tags != []:
# 					if key == tags[0]:
# 						pass
# 					elif salad_dict[key] == None:
# 						salad_dict[key] = tags
# 					else:
# 						salad_dict[key].extend(tags)
# 	return salad_dict


# def get_top_methods(long_dict):
# 	for key in long_dict:
# 		methods = long_dict[key]
# 		VBN = []
# 		if methods != None:
# 			for method in methods:

# 				VBN.append(method[0])
# 			cVBN = Counter(VBN)
# 			topVBN = [ite for ite, it in cVBN.most_common(1)]
# 			long_dict[key] = topVBN[0]
# 	return long_dict


# def pickle_it(short_dict):
# 	with open('saladmethoddict.pickle', 'wb') as handle:
# 		pickle.dump(short_dict, handle)


# raw_list = raw_list()
# long_dict = full_method_dict(raw_list, salad_ingredients)
# short_dict = get_top_methods(long_dict)
# pickle_it(short_dict)
