base = [['chicken broth','chicken stock'],['beef broth','beef stock'],['vegetable broth','vegetable stock'],['cream','milk'],'water','coconut milk','egg noodles']
fats = ['butter','vegetable oil','canola oil','olive oil']
starch = ['toast','potato','sweet potato','butternut squash','couscous',['pasta','noodles','elbows','penne','bow ties'],'tortilla strips','rice','glass noodles','rice noodles']
meat = ['mussels',['beef','sirloin','roast'],'pork','sausage','chorizo','chicken','turkey','clams','bacon']
spices = ['chili powder','white wine','red wine','brown sugar','curry','basil','rosemary','cumin','garlic','cinnamon','ginger','cloves','fennel','thyme','saffrom']
vegetables = ['tomato','zucchini','kale','cabbage','spinach','corn','carrots','onion','red onion','white onion','yellow onion','tomatillos','celery','bell pepper','broccoli']
legumes = ['kidney beans','black beans','peas','lima beans','lentils','jalapeno','seaweed']
toppings = ['cheese','sour cream','cilantro','lime','green onions','avocado']

""" storing here"""
extra_units = ['tablespoons', 'half','to', 'into', 'for', 'cup', 'cups', 'teaspoons', 'tablespoon', 'teaspoon', 'ripe', 'fresh', 'freshly', 'squeezed', 'frozen', 'or', 'and', 'canned', 'cubes', 'diced', 'scoop', 'powdered','such', 'handful', 'pinch', 'in']
methods = ['cut', 'chooped', 'removed', 'garnish', 'optional', 'pitted']

one = ['tomatoes', 'cherry tomatoes', 'red onion', 'broccoli', 'bacon', 'cheddar', 'pepper', 'cucumber', 'red onion', 'cranberries', 'lemon', 'almonds', 'chicken', 'garlic', 'basil', 'mint', 'pepper', 'couscous', 'kidney beans', 'tomatoes', 'corn', 'cheddar', 'egg', 'pepper', 'parsley', 'cayenne pepper', 'lime', 'jicama', 'red onion', 'carrots', 'cilantro', 'pepper', 'lima beans', 'apple', 'celery', 'bacon', 'chicken', 'parmesan', 'pepper', 'cantaloupe', 'feta cheese', 'mint', 'mango', 'kiwi', 'lime', 'bacon', 'steak', 'chicken', 'cilantro', 'garlic', 'pepper', 'scallion', 'mango', 'kiwi', 'lemon', 'egg', 'mint', 'strawberries', 'cantaloupe', 'kiwi', 'lime', 'mint', 'peppers', 'sausage', 'jack', 'mozzarella', 'egg', 'pepper', 'cranberries', 'walnuts', 'beets', 'avocado', 'beets', 'goat cheese', 'pepper', 'apple', 'beets', 'beets', 'goat cheese', 'garlic', 'pepper', 'apple', 'lemon', 'mint', 'lemon', 'mint', 'dates', 'bacon', 'apple', 'orange', 'lime', 'radishes', 'red onion', 'cilantro', 'pepper', 'grapes', 'red onion', 'chicken', 'pepper', 'couscous', 'salami', 'parmesan', 'egg', 'garlic', 'pepper', 'parsley', 'egg', 'lime', 'sweet potato', 'red onion', 'chicken', 'cilantro', 'garlic', 'pepper', 'quinoa', 'soy sauce', 'onions', 'egg', 'pepper', 'croutons', 'watermelon', 'cantaloupe', 'lemon', 'mint', 'cashews', 'soy sauce', 'sesame oil', 'bok choy', 'pepper', 'lime', 'soy sauce', 'sesame oil', 'shrimp', 'garlic', 'ginger', 'lime', 'jicama', 'cilantro', 'pepper', 'apple', 'pumpkin seeds', 'yam', 'bacon', 'scallion', 'alfalfa', 'sprouts', 'shrimp', 'cilantro', 'mint', 'pear', 'almonds', 'tomatoes', 'cherry tomatoes', 'peppers', 'mint', 'pepper', 'parsley', 'couscous', 'lima beans', 'lemon', 'bacon', 'garlic', 'parsley', 'lemon', 'tomatoes', 'cilantro', 'mint', 'pepper', 'parsley', 'scallion', 'couscous', 'onions', 'red onion', 'pepper', 'parsley', 'lima beans', 'lemon', 'salmon', 'garlic', 'pepper', 'parsley', 'garbanzo beans', 'lemon', 'zucchini', 'red onion', 'corn', 'parmesan', 'pepper', 'kidney beans', 'chicken', 'garlic', 'pepper', 'cayenne pepper', 'orange', 'garlic', 'pepper', 'chickpeas', 'sausage', 'garlic', 'pepper', 'lemon', 'lime', 'tomatoes', 'peppers', 'avocado', 'red onion', 'corn', 'garlic', 'pepper', 'cayenne pepper', 'tomatoes', 'cucumber', 'red onion', 'pepper', 'lemon', 'walnuts', 'celery', 'pepper', 'parsley', 'scallion', 'lemon', 'pecans', 'tomatoes', 'broccoli', 'basil', 'pepper', 'mango', 'lemon', 'pumpkin seeds', 'pepper', 'lemon', 'olives', 'red onion', 'parmesan', 'pepper', 'lemon', 'tomatoes', 'cherry tomatoes', 'olives', 'red onion', 'parmesan', 'garlic', 'pepper', 'parsley', 'pine nuts', 'tomatoes', 'cherry tomatoes', 'basil', 'pepper', 'apple', 'strawberries', 'pear', 'mango', 'grapes', 'lemon', 'walnuts', 'pepper', 'red onion', 'pepper', 'orange', 'walnuts', 'basil', 'pepper', 'broccoli', 'bacon', 'peppers', 'olives', 'turkey', 'salami', 'provolone', 'garlic', 'basil', 'pepper', 'black beans', 'lime', 'red onion', 'corn', 'pepper', 'garbanzo beans', 'lemon', 'tomatoes', 'red onion', 'chicken', 'basil', 'mint', 'pepper', 'cranberries', 'almonds', 'tomatoes', 'cherry tomatoes', 'broccoli', 'bacon', 'pepper', 'almonds', 'cucumber', 'chicken', 'feta cheese', 'garlic', 'pepper', 'parsley', 'scallion', 'quinoa', 'eggplant', 'zucchini', 'peppers', 'onions', 'mushrooms', 'asparagus', 'egg', 'garlic', 'basil', 'pepper', 'parsley', 'asparagus', 'egg', 'pepper', 'lime', 'radishes', 'tofu', 'jack', 'mozzarella', 'cilantro', 'pepper', 'scallion', 'soy sauce', 'sesame oil', 'cabbage', 'carrots', 'tofu', 'egg', 'cilantro', 'ginger', 'pepper', 'scallion', 'coconut', 'almonds', 'cauliflower', 'garlic', 'ginger', 'tomatoes', 'eggplant', 'zucchini', 'feta cheese', 'egg', 'mint', 'pepper', 'lemon', 'pine nuts', 'zucchini', 'asparagus', 'egg', 'garlic', 'basil', 'pepper', 'parsley', 'zucchini', 'mushrooms', 'pepper', 'chickpeas', 'tomatoes', 'zucchini', 'carrots', 'cilantro', 'pepper', 'soy sauce', 'bok choy', 'corn', 'tofu', 'garlic', 'ginger', 'pepper', 'scallion', 'chickpeas', 'lemon', 'tomatoes', 'red onion', 'shrimp', 'garlic', 'pepper', 'cayenne pepper', 'tomatoes', 'chicken', 'parmesan', 'garlic', 'basil', 'pepper', 'tomatoes', 'cherry tomatoes', 'bacon', 'parmesan', 'pepper', 'parsley', 'lime', 'almonds', 'carrots', 'salmon', 'mint', 'pepper', 'soy sauce', 'sesame oil', 'mushrooms', 'corn', 'chicken', 'egg', 'garlic', 'ginger', 'pepper', 'scallion', 'celery', 'carrots', 'chicken', 'blue cheese', 'pepper', 'soy sauce', 'tomatoes', 'broccoli', 'corn', 'steak', 'chicken', 'garlic', 'ginger', 'tomatoes', 'olives', 'chicken', 'parmesan', 'mozzarella', 'egg', 'garlic', 'basil', 'pepper', 'onions', 'chicken', 'sausage', 'parmesan', 'garlic', 'pepper', 'celery', 'chicken', 'sausage', 'garlic', 'pepper', 'lemon', 'walnuts', 'chicken', 'parmesan', 'egg', 'garlic', 'basil', 'pepper', 'parsley', 'lemon', 'mushrooms', 'beef', 'egg', 'pepper', 'parsley', 'steak', 'egg', 'pepper', 'cayenne pepper', 'onions', 'mushrooms', 'beef', 'turkey', 'jack', 'pepper', 'apple', 'lemon', 'corn', 'parmesan', 'garlic', 'pepper', 'lemon', 'onions', 'chicken', 'sausage', 'garlic', 'pepper', 'strawberries', 'coconut', 'lemon', 'coconut', 'mango', 'lime', 'almonds', 'apple', 'peanuts', 'cranberries', 'orange', 'apple', 'honeydew', 'apple', 'pineapple', 'strawberries', 'orange', 'mango', 'strawberries', 'orange', 'lime', 'ginger', 'strawberries', 'orange', 'watermelon', 'peanuts', 'ham', 'ham', 'pear', 'orange', 'grapes', 'apple', 'dates', 'lemon', 'almonds', 'pepper', 'orange', 'lemon', 'red onion', 'bacon', 'pepper', 'peanuts', 'corn', 'ham', 'ham', 'egg', 'orange', 'ginger', 'pepper', 'strawberries', 'orange']
two = ['kidney beans', 'tomatoes', 'corn', 'cheddar', 'egg', 'pepper', 'parsley', 'cayenne pepper', 'mango', 'kiwi', 'bacon', 'steak', 'chicken', 'cilantro', 'garlic', 'pepper', 'scallion', 'strawberries', 'cantaloupe', 'kiwi', 'mint', 'apple', 'beets', 'beets', 'goat cheese', 'garlic', 'pepper', 'dates', 'bacon', 'salami', 'parmesan', 'egg', 'garlic', 'pepper', 'parsley', 'sweet potato', 'red onion', 'chicken', 'cilantro', 'garlic', 'pepper', 'quinoa', 'cashews', 'soy sauce', 'sesame oil', 'bok choy', 'pepper', 'jicama', 'cilantro', 'pepper', 'lima beans', 'lemon', 'bacon', 'garlic', 'parsley', 'garbanzo beans', 'lemon', 'zucchini', 'red onion', 'corn', 'parmesan', 'pepper', 'lemon', 'tomatoes', 'peppers', 'avocado', 'red onion', 'corn', 'garlic', 'pepper', 'cayenne pepper', 'mango', 'lemon', 'pumpkin seeds', 'pepper', 'apple', 'strawberries', 'pear', 'mango', 'grapes', 'lemon', 'walnuts', 'pepper', 'peppers', 'olives', 'turkey', 'salami', 'provolone', 'garlic', 'basil', 'pepper', 'almonds', 'cucumber', 'chicken', 'feta cheese', 'garlic', 'pepper', 'parsley', 'scallion', 'quinoa', 'soy sauce', 'sesame oil', 'cabbage', 'carrots', 'tofu', 'egg', 'cilantro', 'ginger', 'pepper', 'scallion', 'zucchini', 'mushrooms', 'pepper', 'tomatoes', 'chicken', 'parmesan', 'garlic', 'basil', 'pepper', 'almonds', 'carrots', 'salmon', 'mint', 'pepper', 'tomatoes', 'olives', 'chicken', 'parmesan', 'mozzarella', 'egg', 'garlic', 'basil', 'pepper', 'lemon', 'mushrooms', 'beef', 'egg', 'pepper', 'parsley', 'lemon', 'onions', 'chicken', 'sausage', 'garlic', 'pepper', 'coconut', 'mango', 'apple', 'honeydew', 'strawberries', 'orange', 'orange', 'lemon', 'red onion', 'bacon', 'pepper']
for entry in one:
	if entry not in two:
		print entry