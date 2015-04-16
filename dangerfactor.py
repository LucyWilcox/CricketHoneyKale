###REMIXX###
# Steps:
# 1. Call the inputted type of food twice or more
# 2. Identify the similarities (3 toppings, 1 dressing)
# 3. Pick 1 or more(depending on danger level) things to swap
# 4. OR/AND add a "danger ingredient list" and add a certain number of those to the recipe
# from saladtoppings import *
# from database_of_recipies import create_recipe_database
# from random import choice, randint
# import pickle
# from database_of_recipies import *
# import re
from smoothies import smoothie_ingredients
from soupingredientsstandard import soup_ingredients
from salad import salad_ingredients
from random import choice, randint


class DangerFactor(object):
    def __init__(self, current_recipe, danger_level):
        self.current_recipe = current_recipe
        self.danger_level = danger_level
        if self.danger_level == 0:
            self.level_zero()
        elif self.danger_level == 1:
            self.level_one()
    def level_zero(self):
        self.new_ingredients = self.current_recipe.toppings

    def level_one(self):
        """Picks a random url and gets the ingredients and instructions. No 
        extra code needed"""
        swap_spot = randint(0,len(self.current_recipe.toppings)-1)
        if self.current_recipe.recipe_type == 'soup':
            new_ingredient = choice(soup_ingredients)
            self.current_recipe.toppings[swap_spot] = new_ingredient
        self.new_ingredients = self.current_recipe.toppings

    def level_two(self):
        """Calls the makerecipe() function of salad.py twice to make two recipes. 
        If after comparing the two, it finds any similarities, it replaces the 
        similarities with random parts of the other recipe. 
        """
        pass

    def level_three(self):
        """Replaces any similar ingredients of 2 recipes of the same food type with
        random choices between the three. If there are no similarities, it 
        replaces random ones with random NEW types of ingredients"""
        pass
    def level_four(self):
        """Introduces another random ingredient without regarding food_type"""
        pass

    def level_five(self):
        """Replaces 1-2 ingredients with danger ingredients"""
        pass



def remix_to_danger(current_recipe):
    print current_recipe.toppings
    danger_recipe = DangerFactor(current_recipe, current_recipe.danger)
    return danger_recipe.new_ingredients
