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
from dangerdanger import danger_ingredients
from random import choice, randint
food_type_databases = [smoothie_ingredients, soup_ingredients, salad_ingredients]

class DangerFactor(object):
    """Creates new_ingredient list which ends up replacing the toppings attribute on RandomRecipe. 
    The severity of the changes depends on the danger level which is passed in from the RandomRecipe object"""
    def __init__(self, current_recipe):
        """Basically selects the correct the danger level to run"""
        self.current_recipe = current_recipe
        self.danger_level = current_recipe.danger
        if self.danger_level == 0:
            self.level_zero()
        elif self.danger_level == 1:
            self.level_one()
        elif self.danger_level == 2:
            self.level_two()
        elif self.danger_level == 3:
            self.level_three()
        elif self.danger_level == 4:
            self.level_four()
        elif self.danger_level == 5:
            self.level_five()        

    def level_zero(self):
        """Just sets the new_ingredients to the old because there should be no change"""
        self.new_ingredients = self.current_recipe.toppings

    def level_one(self):
        """Swaps one ingredient with a random choice within food_type"""
        swap_spot = randint(0,len(self.current_recipe.toppings)-1)
        if self.current_recipe.recipe_type == 'soup':
            new_ingredient = choice(soup_ingredients)
            self.current_recipe.toppings[swap_spot] = new_ingredient
        if self.current_recipe.recipe_type == 'smoothie':
            new_ingredient = choice(smoothie_ingredients)
            self.current_recipe.toppings[swap_spot] = new_ingredient
        if self.current_recipe.recipe_type == 'salad':
            new_ingredient = choice(salad_ingredients)
            self.current_recipe.toppings[swap_spot] = new_ingredient
        if self.current_recipe.recipe_type == 'sandwich':
            new_ingredient = choice(sandwich_ingredients)
            self.current_recipe.toppings[swap_spot] = new_ingredient
        self.new_ingredients = self.current_recipe.toppings

    def level_two(self):
        """Replace an ingredient with a random ingredient without
        regarding food_type"""
        swap_spot = randint(0,len(self.current_recipe.toppings)-1)
        extra_ingredient_type = choice(food_type_databases)
        new_ingredient = choice(extra_ingredient_type)
        self.current_recipe.toppings[swap_spot] = new_ingredient
        self.new_ingredients = self.current_recipe.toppings

    def level_three(self):
        """Replaces 2 ingredients in the recipe: one being in the food type 
        and one danger ingredient"""
        swap_spot_1 = randint(0,len(self.current_recipe.toppings)-1)
        swap_spot_2 = randint(0,len(self.current_recipe.toppings)-1)
        while swap_spot_1 == swap_spot_2:
            swap_spot_2 = randint(0,len(self.current_recipe.toppings)-1)
        if self.current_recipe.recipe_type == 'soup':
            new_ingredient = choice(soup_ingredients)
            self.current_recipe.toppings[swap_spot_1] = new_ingredient
        if self.current_recipe.recipe_type == 'smoothie':
            new_ingredient = choice(smoothie_ingredients)
            self.current_recipe.toppings[swap_spot_1] = new_ingredient
        if self.current_recipe.recipe_type == 'salad':
            new_ingredient = choice(salad_ingredients)
            self.current_recipe.toppings[swap_spot_1] = new_ingredient
        if self.current_recipe.recipe_type == 'sandwich':
            new_ingredient = choice(sandwich_ingredients)
            self.current_recipe.toppings[swap_spot_1] = new_ingredient
        self.current_recipe.toppings[swap_spot_2] = choice(danger_ingredients)
        self.new_ingredients = self.current_recipe.toppings
    
    def level_four(self):
        """Replaces 2 ingredients in the recipe: one not specifically in the 
        food type, and one danger ingredient"""
        swap_spot_1 = randint(0,len(self.current_recipe.toppings)-1)
        swap_spot_2 = randint(0,len(self.current_recipe.toppings)-1)
        while swap_spot_1 == swap_spot_2:
            swap_spot_2 = randint(0,len(self.current_recipe.toppings)-1)
        extra_ingredient_type = choice(food_type_databases)
        new_ingredient = choice(extra_ingredient_type)
        self.current_recipe.toppings[swap_spot_1] = new_ingredient
        self.current_recipe.toppings[swap_spot_2] = choice(danger_ingredients)
        self.new_ingredients = self.current_recipe.toppings

    def level_five(self):
        """Replaces 1-2 ingredients with danger ingredients"""
        swap_spot_1 = randint(0,len(self.current_recipe.toppings)-1)
        swap_spot_2 = randint(0,len(self.current_recipe.toppings)-1)
        while swap_spot_1 == swap_spot_2:
            swap_spot_2 = randint(0,len(self.current_recipe.toppings)-1)
        self.current_recipe.toppings[swap_spot_1] = choice(danger_ingredients)
        self.current_recipe.toppings[swap_spot_2] = choice(danger_ingredients)        
        self.new_ingredients = self.current_recipe.toppings

def remix_to_danger(current_recipe):
    danger_recipe = DangerFactor(current_recipe)
    return danger_recipe.new_ingredients
