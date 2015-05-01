from saladtoppings import salad_ingredients
from soupingredientsstandard import soup_ingredients
from dangerdanger import danger_ingredients
from sandwich_ingredients import sandwich_ingredients
from database_of_recipies import *
from nltk import word_tokenize, pos_tag
from collections import Counter
import pickle


class PrepDict(object):
    """Creates dictionary of prep, both for methods and amounts"""
    def __init__(self, recipes, ingredients_used, file_name, pos):
        """pos is part of speach which is used to find measurement amounds and methods
        recipes is all recipe objects created in database_of_recipies
        ingredients_used is all unique ingredients
        file name is where the file will be pickled/saved"""
        self.pos = pos
        self.recipes = recipes
        self.ingredients_used = ingredients_used #list of pre-defined ingredients
        self.file_name = file_name

    def get_raw_list(self):
        """Splits in ingredient step in the recipe into different entries in a list"""
        each_ingredient = []
        for recipe in self.recipes:
            seperated_ingredients = recipe.ingredients.replace(',', '').replace(']','').split("*") #splits full recipe string into seperate ingerdients strings
            each_ingredient.extend(seperated_ingredients)
        each_ingredient = filter(lambda a: a != '[', each_ingredient)
        self.raw_list = each_ingredient

    def full_method_dict(self):
        """Creates dictionary of all ingredients and their preperation methods """
        def each_prep_methods(method, ingredients_used):
            """Returns list of strings of appropriate preperation methods"""
            blacklist = ['recommended', 'beaten', 'frozen', 'red', 'kitchen']
            text = word_tokenize(method) #seperates ingredient strings into lists of each word in the string
            tags = pos_tag(text) #converts list into list of tuples like (text, part of speach)
            good_types = []
            for tag in tags:  #tag[1] is the pos, tag[0] is the word
                if tag[1] in self.pos and tag[0] not in ingredients_used and tag[1] not in blacklist: #we want tag[0] to be the correct pos, but we don't want it to be refering directly to the ingredient or one our blacklisted/buggy words
                    good_types.append(tag[0])
            return good_types
        def each_amount_methods(method, ingredients_used):
            """Returns list of  strings of reasonable quanities of ingredient"""
            #need to hard code in some meaurements here
            measurements = ['tablespoons', 'cup', 'cups', 'teaspoons', 'tablespoon', 'teaspoon', 'pinch', 'ounce', 'oz', 'pint', 'ounces', 'spoonfuls', 'large', 'small', 'pieces', 'pounds']
            text = word_tokenize(method) #seperates ingredient strings into lists of each word in the string
            tags = pos_tag(text) #converts list into list of tuples like (text, part of speach)
            good_amounts = []
            amount_str = ""
            for tag in tags:
                if tag[1] in self.pos or tag[0] in measurements: 
                    amount_str = amount_str + tag[0] + " "
            new_amount_str = amount_str.replace(")", "")
            good_amounts.append(new_amount_str)
            return good_amounts

        method_dict = dict.fromkeys(self.ingredients_used) #creates dictonary of prelisted ingredients as keys
        for method in self.raw_list: #method is each line in the ingedients Food Network section
            for key in method_dict:
                if key in method: # so if the ingredient (expressed as a key) is in the method then it is relvant to anaylize for that key
                    if self.file_name == 'methoddict.pickle':
                        tags = each_prep_methods(method, self.ingredients_used)  #looks at the relvant ingredient instruction line to find correct method
                    else:
                        tags = each_amount_methods(method, self.ingredients_used)

                    if tags != []:
                        if method_dict[key] == None:
                            method_dict[key] = tags #adds correct method(s) as values if there are no current values
                        else: 
                            method_dict[key].extend(tags) #adds correct method to existing list
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
        if value not in seen:
            output.append(value)
            seen.add(value)
    return output

if __name__ == '__main__':
    with open('themrecipies.pickle', 'rb') as handle:
        recipes = pickle.load(handle)
    all_ingredients = salad_ingredients + soup_ingredients + danger_ingredients +  sandwich_ingredients #compiles list of all ingredient being used
    culled_ingredients = remove_duplicates(all_ingredients)
    verbs = PrepDict(recipes, culled_ingredients, 'methoddict.pickle', ['VBN', 'VBD'])
    verbs.get_raw_list()
    verbs.full_method_dict()
    verbs.get_top_methods()
    verbs.pickle_it()
    amounts = PrepDict(recipes, culled_ingredients, 'amountdict.pickle', ['LS', 'CD'])
    amounts.get_raw_list()
    amounts.full_method_dict()
    amounts.get_top_methods()
    amounts.pickle_it()




