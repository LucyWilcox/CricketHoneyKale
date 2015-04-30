"""Uncommment imports if running this file"""
#from bs4 import BeautifulSoup as BS 
#import requests
#from pattern.web import plaintext
#from recipedatabase import recipe_database
#from string import find, split
#import cPickle as pickle

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

def create_recipe_database():
    """Creates the pickle file"""
    recipes = []
    for url in recipe_database[: len(recipe_database) - 1]:
        recipes.append(Recipe(url))

    with open('themrecipies.pickle', 'wb') as handle:
        pickle.dump(recipes, handle)

    return recipes


if __name__ == '__main__':
    recipes =  create_recipe_database()