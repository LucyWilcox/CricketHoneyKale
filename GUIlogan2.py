#!/usr/bin/env python3
import Tkinter as tk  
from salad import *
from os.path import exists

class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()  
        self.master = master
        master.minsize(width=850, height=300)
        self.run()

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
        title = tk.Label(self.master, text = "Let's Cook Something!!")
        info = tk.Button(self.master, text="Information", command = self.pressinfo)

        title.grid(row=0, column=1, padx=20, columnspan=2)
        info.grid(row=0, column=0)

    def pressinfo(self):
        top = tk.Toplevel()
        top.title("Information")
        disc = tk.Label(top, text = infotext )
        disc.grid()

    def quitButton(self):
        quit = tk.Button(self.master, text='Quit',command=self.quit)
        quit.grid(row=0, column=3, padx=20, pady=30)
          
    def display_recipe(self, want_to_cook):
        dan = self.checkdanger()
        al = self.checkallergy()

        recipe_directions = make_recipe(want_to_cook, dan )

        top = tk.Toplevel()
        top.title("Recipe")
        top.resizable(0,0)
        rec = tk.Label(top, text = recipe_directions )
        rec.grid(row=2,column=1, pady=35, padx=35)

    def danger(self):     
        value = tk.StringVar()
        dangerdescript = tk.Label(self.master, text="how dangerous are you? ")
        dangerdescript.grid(row=2, column=0)
        dang = tk.Spinbox(self.master,textvariable=value,from_=0, to=5, width = 3)
        dang.grid(row=2, column=1)
        but = tk.Button(self.master, text='get dangerous',command=self.getdanger)
        but.grid(row=2, column=2, padx=20, pady=30)
        self.value = value
        dlevel = tk.Label(self.master, text="Current danger level is "  )
        dlevel.grid(row=2, column=3)

    def allergy(self): 
        ingred = tk.StringVar()
        allerdescript = tk.Label(self.master, text="enter allergens seperated by commas:")
        allerdescript.grid(row=3, column=0)
        aller = tk.Entry(self.master, textvariable=ingred)
        aller.grid(row=3, column=1)
        butt = tk.Button(self.master, text='record allergens', command=self.getallergy)
        butt.grid(row=3,column=2)
        alist = tk.Label(self.master, text="Allergens: "  )
        alist.grid(row=3, column=3)

        # allergens will be the second string input in recipe directions
        # if ther is no allergens give an empty string

    def checkdanger(self):
        if hasattr(self, "dangervalue"):
            d = self.dangervalue
        else:
            d = 0
        return d
    def checkallergy(self):
        if hasattr(self, "allergyvalue"):
            a = self.allergyvalue
        else: 
            a = ""
        return a

    def getdanger(self):
        value = self.value
        self.dangervalue = value.get()
        ya = value.get()
        #print type(self.dangervalue)
    def getallergy(self):
        ingred = self.ingred
        self.allergyinfo = ingred.get()      

    def run(self):
        self.foodbuttons()
        self.words()
        self.quitButton()
        self.danger()
        self.allergy()
        #self.pressdisclaimer()

infotext = """Please be safe. 
        We are not responsible for food poisioning, allergic reactions, broken blenders, gross recipes or anything else.  
        A CricketHoneyKale creation by Lucy Wilcox, Lisa Hachmann, and Logan Sweet. 
        Please direct all negative feedback to byron.wasti@students.olin.edu"""
       

root = tk.Tk()
app = Application(root)
app.master.title('CricketHoneyKale')
root.mainloop()


     

# if __name__ == '__main__':
#     root = Tk
#     #app.master.title('I hope this works')
#     ex = Application(root)
#     root.mainloop()
