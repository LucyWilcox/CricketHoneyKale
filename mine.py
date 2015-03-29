#This dumps the HTML of a website into the variable s. Put the desired URL in the variable "theURL." 

from os.path import exists
import sys
from pickle import dump, load
from pattern.web import URL, plaintext
 
#replace theURL with the URL you wan to evaluate 
theURL = 'http://www.foodnetwork.com/recipes/food-network-kitchens/spanish-chicken-and-potato-roast-recipe.html'
s = URL(theURL).download()
s = plaintext(s, keep={'h1':[], 'h2':[], 'strong':[], 'a':['href']})
#print s

file_name = "recipe.html"                  #replace the file extension with whatever kind of save you want (subl,txt,html...)
if exists(file_name):                   
	data = load(open(file_name, "r+"))  
	data = s                            
else:                                   
	data = s                            
	
<<<<<<< HEAD
dump (data, open(file_name, "w+"))         # write the info in data to the file   
=======
#dump (data, open(file_name, "w+"))         # write the info in data to the file   
>>>>>>> 0fe02ad4bcd587b1d13ac9d0e5aa0e6e73c21f0f
#return data  
