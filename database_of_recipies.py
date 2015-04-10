from bs4 import BeautifulSoup as BS
import requests
import xml.etree.ElementTree
from pattern.web import plaintext
from recipedatabase import recipe_database
from string import find, split
import cPickle as pickle

class Recipe(object):
    """ """
    def __init__(self, url):
        """Sets attributes of url and ingredient with amounts to each recipe"""
        self.url = url
        r = requests.get(self.url)
        data = r.text   
        soup = BS(data)
        gross_ingredients = str(soup.find_all("li", {"itemprop":"ingredients"}))
        self.ingredients = str(plaintext(gross_ingredients).replace('\n', '').lower())

    def is_ingredient_used(self, ingredient):
        """ If the ingredient is used in a recipe an attribuet ingredient_used is 
        set to True, else False """
        if ingredient in self.ingredients:
            self.ingredient_used = True
        else:
            self.ingredient_used = False
        #return self.ingredient_used

    def pickle_it(self):
        f = file('recipe_data.pk1', 'wb')
        pickle.dump(self, f, pickle.HIGHEST_PROTOCOL)
        f.close()

def create_recipe_database():
    recipes = []
    for url in recipe_database[:20]: #len(recipe_database) - 1]:
        recipes.append(Recipe(url))

    # for recipe in recipes:
    #     recipe.pickle_it()

    #output = open('recipe_data.pk1', 'wb')
    #pickle.dump(recipes, output, pickle.HIGHEST_PROTOCOL)
    return recipes



recipes =  create_recipe_database()