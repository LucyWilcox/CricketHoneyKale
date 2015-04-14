base = ['chicken broth','chicken stock','beef broth','beef stock','vegetable broth','vegetable stock','cream','milk','water','coconut milk','egg noodles']
fats = ['butter','vegetable oil', 'sesame oil', 'canola oil','olive oil']
starch = ['potato','sweet potato','butternut squash','couscous','pasta','noodles','elbows','penne','bow ties','tortilla strips','rice','glass noodles','rice noodles']
protein = ['mussels','beef','sirloin','roast','pork','sausage','chorizo','chicken','turkey','clams','bacon', 'tofu']
spices = ['soy sauce', 'chili sauce', 'chili powder','white wine','red wine','brown sugar','curry','basil','rosemary','cumin','garlic','cinnamon','ginger','cloves','fennel','thyme','saffron']
vegetables = ['tomato', 'water cress', 'eggplant', 'yam', 'artichoke', 'bok choy', 'cherry tomatoes', 'spaghetti squash', 'snow peas', 'peppers', 'mushrooms', 'cauliflower', 'celery', 'cucumber', 'alfalfa', 'sprouts', 'asparagus', 'avocado', 'red onion', 'beets', 'broccoli', 'bean sprouts', 'brussel sprouts', 'baby corn', 'zucchini','kale','cabbage','spinach','corn','carrots','onion', 'white onion','yellow onion','tomatillos', 'bell pepper']
beans = ['garbanzo beans', 'chickpeas', 'lentils', 'kidney beans', 'lima beans', 'black eye peas', 'black beans']
toppings = ['cheese','sour cream', 'green onions','jalapeno','seaweed', 'cilantro', 'mint', 'pepper', 'parsley', 'scallion', 'cayenne pepper']


soup_ingredients = base + fats + starch + protein + spices + vegetables + beans + toppings

def remove_duplicates(values):
    output = []
    seen = set()
    for value in values:
        # If value has not been encountered yet,
        # ... add it to both list and set.
        if value not in seen:
            output.append(value)
            seen.add(value)
        else:
        	pass
         	print value
    return output