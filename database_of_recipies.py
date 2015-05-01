"""Uncommment imports if running this file"""
#from bs4 import BeautifulSoup as BS 
#import requests
#from pattern.web import plaintext
#from recipedatabase import recipe_database
#from string import find, split
#import cPickle as pickle

class Recipe(object):
    """Creates instances of Recipe for each Food Network recipe in recipedatabase"""
    def __init__(self, url):
        """Sets attributes of url and ingredient to each recipe
        self.ingredient is the string containing the information listed under the Ingredients
        section on Food Networks web pages"""
        self.url = url
        r = requests.get(self.url) #gets html from webpage
        data = r.text   
        soup = BS(data)
        gross_ingredients = str(soup.find_all("li", {"itemprop":"ingredients"})) #extracts corrects data from Food Network webpage
        self.ingredients = str(plaintext(gross_ingredients).replace('\n', '').lower()) #strips some remaining html and changes things to lower case


def create_recipe_database():
    """Creates the pickle file, so this does not need to be run for each recipe created"""
    recipes = []
    for url in recipe_database[: len(recipe_database) - 1]:
        recipes.append(Recipe(url))
    with open('themrecipies.pickle', 'wb') as handle:
        pickle.dump(recipes, handle)
    return recipes


if __name__ == '__main__':
    recipes =  create_recipe_database()