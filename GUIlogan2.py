#!/usr/bin/env python3
import Tkinter as tk  
from salad import *
from os.path import exists

class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()  
        self.master = master
        self.run()
        #self.placeWidgets()

    def foodbuttons(self):
        # recipe_directions.grid_forget()
        soup = tk.Button(self.master, text = 'Generate me a soup!', command = lambda:self.display_recipe('soup'))
        salad = tk.Button(self.master, text = 'Generate me a salad!', command = lambda:self.display_recipe('salad'))
        smoothie = tk.Button(self.master, text = 'Generate me a smoothie!', command = lambda:self.display_recipe('smoothie'))
        sandwich = tk.Button(self.master, text = 'Generate me a sandwich!', command = lambda:self.display_recipe('sandwich'))

        soup.grid(row=1,column=0, padx=20)
        salad.grid(row=1,column=1, padx=20)
        smoothie.grid(row=1,column=2, padx=20)
        sandwich.grid(row=1,column=3, padx=20)

    def words(self):
        feedback = tk.Label(self.master, text = " A CricketHoneyKale creation by Lucy Wilcox, Lisa Hachmann, and Logan Sweet. Please direct all negative feedback to byron.wasti@students.olin.edu")
        title = tk.Label(self.master, text = "Let's Cook Something!!")
        bottom = tk.Label(self.master, text = ' ')
        disclaimer = tk.Label(self.master, text = "\n\nPlease be safe. \n We are not responsible for food poisioning, allergic reactions, broken blenders, gross recipes or anything else.")

        feedback.grid(row=7,column=0,columnspan=4, pady=0)
        title.grid(row=0, column=1, padx=20, columnspan=2)
        disclaimer.grid(row=6,column=0,columnspan=4, pady=10)
        #bottom.grid(row = 7, pady = 15)

    def quitButton(self):
        quit = tk.Button(self.master, text='Quit',command=self.quit)
        quit.grid(row=0, column=3, padx=20, pady=30)
          
    def display_recipe(self, want_to_cook):

        if hasattr(self, "dangervalue"):
            recipe_directions = make_recipe(want_to_cook, self.dangervalue)
        else: 
            recipe_directions = make_recipe(want_to_cook, 0)
       
        instructions = tk.Label(self.master, text = recipe_directions)
        instructions.grid(row=5, column=0, columnspan=4, pady=75)
        # instructions = tk.Label(self.master, text = " ")
        # #instructions.grid(row=4, column=0, columnspan=4, pady=75)
        # instructions.grid_remove()

    def box(self):     
        value = tk.StringVar()
        dangerbox = tk.Spinbox(self.master,textvariable=value,from_=0, to=5)
        dangerbox.grid(row=2, column=1)
        but = tk.Button(self.master, text='get dangerous',command=self.obtener)
        but.grid(row=2, column=2, padx=20, pady=30)
        self.value = value
   

    def allergy(self): 
        aller = tk.Entry(self.master)
        aller.grid(row=4, column=2)
        allerinst = tk.Label(self.master, text="enter allergens seperated by commas:")
        allerinst.grid(row=4, column=1)
        # allergens will be the second string input in recipe directions
        # if ther is no allergens give an empty string

        


    def obtener(self):
        value = self.value
        self.dangervalue = value.get()
      




    def run(self):
        self.foodbuttons()
        self.words()
        self.quitButton()
        self.box()
        self.allergy()
       

root = tk.Tk()
app = Application(root)
app.master.title('I hope this works')
root.mainloop()


# if __name__ == '__main__':
#     root = Tk
#     #app.master.title('I hope this works')
#     ex = Application(root)
#     root.mainloop()
