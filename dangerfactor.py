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
# from smoothies import *
#from salad import *
from salad import make_recipe


class DangerFactor(object):
    def __init__(self, food_type, danger_level):
        self.food_type = food_type
        self.danger_level = danger_level

    def level_one(self):
        """Picks a random url and gets the ingredients and instructions. No 
        extra code needed"""
        pass

    def level_two(self):
        """Calls the makerecipe() function of salad.py twice to make two recipes. 
        If after comparing the two, it finds any similarities, it replaces the 
        similarities with random parts of the other recipe. 
        """
        """For when you get ingredients in a string of instructions
        Known problem that two part words are lost in the splitting process"""
        current_salad_1 = []
        current_smoothie_1 = []
        current_salad_2 = []
        current_smoothie_2 = []
        instruction1 = make_recipe(self.food_type).replace('!', '').replace(',', '').replace(':', '').split()
        instruction2 = make_recipe(self.food_type).replace('!', '').replace(',', '').replace(':', '').split()
        for word in instruction1:
            if word in smoothie_ingredients and self.food_type == 'smoothie':
                current_smoothie_1.append(word)
            if word in salad_ingredients and self.food_type == 'salad':
                current_salad_1.append(word)
        for word in instruction2:
            if word in smoothie_ingredients and self.food_type == 'smoothie':
                current_smoothie_2.append(word)
            if word in salad_ingredients and self.food_type == 'salad':
                current_salad_2.append(word)
        for i in range(len(current_smoothie_1)):
            for j in range(len(current_smoothie_2)):
                if current_smoothie_1[i] == current_smoothie_2[j]:
                    current_smoothie_1[i] = choice(current_smoothie_2)
                    current_smoothie_2[j] = choice(current_smoothie_1)
        return current_smoothie_1
        """For when you get ingredients in a list of strings'"""
        # first_remix = make_recipe(food_type)
        # second_remix = make_recipe(food_type)
        # print first_remix
        # print second_remix
        # for i in range(len(first_remix)):
        #   for j in range(len(second_remix)):
        #       if first_remix[i] == second_remix[j]:
        #           first_remix[i] = choice(second_remix)
        #           second_remix[j] = choice(first_remix)
        # return first_remix, second_remix

    def level_three(self):
        """Replaces any similar ingredients of 2 recipes of the same food type with
        random choices between the three. If there are no similarities, it 
        replaces random ones with random NEW types of ingredients"""
        first_recipe= make_recipe(self.food_type)
        second_recipe = make_recipe(self.food_type)
        for i in range(len(first_recipe)):
            for j in range(len(second_recipe)):
                if first_recipe[i] == second_recipe[j]:
                    first_recipe[i] = choice(second_recipe)
                    second_recipe[j] = choice(first_recipe)
                    first_remix = first_recipe
                    second_remix = second_recipe

    def level_four(self, food_type):
        """Introduces another random ingredient of it's same food_type"""
        pass

    def level_five(self, food_type):
        """Replaces half of the ingredients with new ones- brand new, no swapping"""
        pass

    def level_six(self, food_type):
        pass

    def level_seven(self, food_type):
        pass

    def level_eight(self, food_type):
        """Randomly selects a chosen random amount of ingredients and pretends it's a recipe
        - stays within it's food type"""
        """Here for storgage right now """
        smoothie_1 = make_recipe(food_type)
        smoothie_2 = make_recipe(food_type)
        print smoothie_1
        print smoothie_2
        for i in range(len(smoothie_1)):
            for j in range(len(smoothie_2)):
                if smoothie_1[i] == smoothie_2[j]:
                    smoothie_1[i] = choice(smoothie_2)
        return smoothie_1

    def level_nine(self, food_type):
        """Randomly selects a chosen random amount of ingredients and pretends it's 
        a recipe- doesn't stay within it's food type"""
        pass

    def level_ten(self, food_type):
        pass

if __name__ == '__main__':
    bizarre_recipe = DangerFactor('smoothie', 8)
    print bizarre_recipe.level_one()