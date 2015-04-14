###REMIXX###
# Steps:
# 1. Call the inputted type of food twice or more
# 2. Identify the similarities (3 toppings, 1 dressing)
# 3. Pick 1 or more(depending on danger level) things to swap
# 4. OR/AND add a "danger ingredient list" and add a certain number of those to the recipe
from saladtoppings import *
from database_of_recipies import create_recipe_database
from random import choice, randint
import pickle
from database_of_recipies import *
import re
from smoothies import *
from salad import *
from salad import make_recipe


print make_recipe('smoothie')