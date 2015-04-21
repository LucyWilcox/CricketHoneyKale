#!/usr/bin/env python3
import Tkinter as tk  
from salad import *

## Some of thee buttons are having issues connecting
## The danger scale needs to be connected to the code
## Maybe put disclaimer in a different window? 
##
 
class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()  
        self.master = master
        self.createWidgets()
        #self.placeWidgets()
 
    def createWidgets(self):
        soup = tk.Button(self.master, text = 'Generate me a soup!', command = lambda:self.display_recipe('soup'))
        salad = tk.Button(self.master, text = 'Generate me a salad!', command = lambda:self.display_recipe('salad'))
        smoothie = tk.Button(self.master, text = 'Generate me a smoothie!', command = lambda:self.display_recipe('smoothie'))
        sandwich = tk.Button(self.master, text = 'Generate me a sandwich!', command = lambda:self.display_recipe('sandwich'))

        feedback = tk.Label(self.master, text = " A CricketHoneyKale creation by Lucy Wilcox, Lisa Hachmann, and Logan Sweet \n Please direct all negative feedback to byron.wasti@students.olin.edu")
        title = tk.Label(self.master, text = "Let's Cook Something!!")
        quit = tk.Button(self.master, text='Quit',command=self.quit)
        disclaimer = tk.Label(self.master, text = "\n\nPlease be safe. \n We are not responsible for food poisioning, allergic reactions, broken blenders, gross recipes or anything else.")
        #danger = tk.Scale(self.master, from_=0, to=5)
        danger = tk.Spinbox(self.master, from_=0, to=5)
        #danger = tk.Scrollbar(self.master)
        instructions = tk.Label(self.master, text = 'INSTRUCTIONS GO HERE OR SOMETHING')
        bottom = tk.Label(self.master, text = ' ')

        

        def placeWidgets():
            feedback.grid(row=6,column=0,columnspan=4, pady=20)
            title.grid(row=0, column=1, padx=20, columnspan=2)
            quit.grid(row=0, column=3, padx=20, pady=30)
            disclaimer.grid(row=5,column=0,columnspan=4)
            danger.grid(row=3,column=1,columnspan=2, pady=30)

            soup.grid(row=1,column=0, padx=20)
            salad.grid(row=1,column=1, padx=20)
            smoothie.grid(row=1,column=2, padx=20)
            sandwich.grid(row=1,column=3, padx=20)

            instructions.grid(row=4, column=0, columnspan=4)
            #bottom.grid(row = 7, pady = 15)

        placeWidgets()


    def display_recipe(self, want_to_cook):
        recipe_directions = make_recipe(want_to_cook, 2)
        return recipe_directions
        # see = tk.Label(self.master, text = recipe_name.instruction_string).grid

root = tk.Tk()
app = Application(root)
app.master.title('I hope this works')
root.mainloop()


# if __name__ == '__main__':
#     root = Tk
#     #app.master.title('I hope this works')
#     ex = Application(root)
#     root.mainloop()
