from saladtoppings import salad_ingredients
from soupingredientsstandard import soup_ingredients
from dangerdanger import danger_ingredients
from sandwich_ingredients import sandwich_ingredients
from database_of_recipies import *
import nltk
import re
from collections import Counter
import pickle


measurements = ['tablespoons', 'cup', 'cups', 'teaspoons', 'tablespoon', 'teaspoon', 'pinch', 'ounce', 'oz', 'pint', 'ounces', 'spoonfuls', 'large', 'small', 'pieces', 'pounds']
blacklist = ['recommended', 'beaten', 'frozen', 'red', 'kitchen']

class PrepDict(object):
    """Creates dictionary of prep, both for methods and amounts"""
    def __init__(self, recipes, ingredients_used, file_name, pos):
        """pos is part of speach which is used to find measurement amounds and methods
        recipes is all recipe objects created in database_of_recipies
        ingredients_used is all unique ingredients
        file name is where the file will be pickled/saved"""
        self.pos = pos
        self.recipes = recipes
        self.ingredients_used = ingredients_used
        self.file_name = file_name

    def get_raw_list(self):
        """Splits in ingredient step in the recipe into different entries in a list"""
        each_ingredient = []
        for recipe in self.recipes:
            seperated_ingredients = recipe.ingredients.replace(',', '').replace(']','').split("*")
            each_ingredient.extend(seperated_ingredients)
        each_ingredient = filter(lambda a: a != '[', each_ingredient)
        self.raw_list = each_ingredient

    def full_method_dict(self):
        """Creates dictionary of all ingredients and their preperation methods """
        def each_prep_methods(method, ingredients_used):
            """Returns list of strings of appropriate preperation methods"""
            text = nltk.word_tokenize(method)
            tags = nltk.pos_tag(text)
            good_types = []
            for tag in tags:
                if tag[1] in self.pos and tag[0] not in ingredients_used and tag [1] not in blacklist:
                    good_types.append(tag[0])
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

    def amount_dict(self):
        """Creates a dictionary of all ingredients and their resonable amounts """
        def each_prep_methods(method, ingredients_used):
            """Returns list of  strings of reasonable quanities of ingredient"""
            text = nltk.word_tokenize(method)
            tags = nltk.pos_tag(text)
            bad_pos = ['(', ')']
            good_amounts = []
            amount_str = ""
            i = 0
            for tag in tags:
                i += 1
                if tag[1] in self.pos or tag[0] in measurements: 
                    if tag[0] in bad_pos:
                        pass
                    else:
                        amount_str = amount_str + tag[0] + " "
            good_amounts.append(amount_str)
            return good_amounts

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
        """Gets top two methods/amounts and creates a dictionary where the top one is listed twice and the
        second most common is listed once"""
        for key in self.long_dict:
            methods = self.long_dict[key]
            VBN = []
            if methods != None:
                for method in methods:
                    if method != '':
                        VBN.append(method)
                cVBN = Counter(VBN)
                topVBN = [ite for ite, it in cVBN.most_common(2)]
                self.long_dict[key] = topVBN[:2]
                self.long_dict[key].append(topVBN[0])


    def pickle_it(self):
        """Pickles the dictionary"""
        with open(self.file_name, 'wb') as handle:
            pickle.dump(self.long_dict, handle)


def remove_duplicates(values):
    """Removes duplicate ingredients """
    output = []
    seen = set()
    for value in values:
        # If value has not been encountered yet,
        # ... add it to both list and set.
        if value not in seen:
            output.append(value)
            seen.add(value)
    return output

if __name__ == '__main__':
    with open('themrecipies.pickle', 'rb') as handle:
        recipes = pickle.load(handle)
    all_ingredients = salad_ingredients + soup_ingredients + danger_ingredients +  sandwich_ingredients
    culled_ingredients = remove_duplicates(all_ingredients)
    # verbs = PrepDict(recipes, culled_ingredients, 'methoddict.pickle', ['VBN'])
    # verbs.get_raw_list()
    # verbs.full_method_dict()
    # verbs.get_top_methods()
    # verbs.pickle_it()
    amounts = PrepDict(recipes, culled_ingredients, 'amountdict.pickle', ['LS', 'CD'])
    amounts.get_raw_list()
    amounts.amount_dict()
    amounts.get_top_methods()
    amounts.pickle_it()
    print amounts.long_dict




