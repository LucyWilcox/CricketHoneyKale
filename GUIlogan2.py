 #!/usr/bin/env python3
import Tkinter as tk  
from main import *

class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()  
        self.master = master
        master.minsize(width=850, height=300)
        self.run()
                                                                                          # activeofreground changes the text color: dont use for buttons
    def foodbuttons(self):
        soup = tk.Button(self.master, text = 'Generate me a soup!', command = lambda:self.display_recipe('soup'),bg='#639BF1', activebackground='#3B5998')
        salad = tk.Button(self.master, text = 'Generate me a salad!', command = lambda:self.display_recipe('salad'),bg='#639BF1', activebackground='#3B5998')
        smoothie = tk.Button(self.master, text = 'Generate me a smoothie!', command = lambda:self.display_recipe('smoothie'),bg='#639BF1', activebackground='#3B5998')
        sandwich = tk.Button(self.master, text = 'Generate me a sandwich!', command = lambda:self.display_recipe('sandwich'),bg='#639BF1', activebackground='#3B5998')

        soup.grid(row=1,column=0, padx=20)
        salad.grid(row=1,column=1, padx=20)
        smoothie.grid(row=1,column=2, padx=20)
        sandwich.grid(row=1,column=3, padx=20)

    def words(self):
        title = tk.Label(self.master, text = "Let's Cook Something!!", bg='#77BA9B')
        info = tk.Button(self.master, text="Information", command = self.pressinfo,bg='#639BF1', activebackground='#3B5998')
        quit = tk.Button(self.master, text='Quit',command=self.quit,bg='#639BF1', activebackground='#3B5998')

        title.grid(row=0, column=1, padx=20, columnspan=2)
        info.grid(row=0, column=0)
        quit.grid(row=0, column=3, padx=20, pady=30)

    def pressinfo(self):
        top = tk.Toplevel()
        top.title("Information")
        disc = tk.Label(top, text = infotext )
        disc.grid()
          
    def display_recipe(self, want_to_cook):
        #recipe_directions = make_recipe(want_to_cook, self.allergyvalue, self.dangervalue)
        recipe_directions = make_recipe(want_to_cook, self.allergyinfo, self.dangervalue)
        top = tk.Toplevel()
        top.title("Recipe")
        top.resizable(0,0)
        rec = tk.Label(top, text = recipe_directions )
        rec.grid(row=2,column=1, pady=35, padx=35)

    def danger(self):     
        value = tk.StringVar()
        dangerdescript = tk.Label(self.master, text="How dangerous are you? " , bg='#77BA9B')
        dangerdescript.grid(row=2, column=0)
        dang = tk.Spinbox(self.master,textvariable=value,from_=0, to=5, width = 3)
        dang.grid(row=2, column=1)
        but = tk.Button(self.master, text='Get Dangerous',command=self.getdanger,bg='#639BF1', activebackground='#3B5998')
        but.grid(row=2, column=2, padx=20, pady=30)
        self.value = value
 
    def allergy(self): 
        ingred = tk.StringVar()
        allerdescript = tk.Label(self.master, text="Enter allergens seperated by commas:", bg='#77BA9B')
        allerdescript.grid(row=3, column=0)
        aller = tk.Entry(self.master, textvariable=ingred)
        aller.grid(row=3, column=1)
        butt = tk.Button(self.master, text='Record Allergens', command=self.getallergy,bg='#639BF1', activebackground='#3B5998')
        butt.grid(row=3,column=2)
        self.ingred = ingred

    def checkdanger(self):
        if hasattr(self, "dangervalue"):
            pass
        else:
            self.dangervalue = 0

    def checkallergy(self):
        if hasattr(self, "allergyvalue"):
            pass
        else: 
            self.allergyinfo = " "
        #print self.allergyinfo

    def getdanger(self):
        value = self.value
        self.dangervalue = value.get()
        #ya = value.get()
        dlevel = tk.Label(self.master, text="Current danger level is " + self.dangervalue , bg='#77BA9B')
        dlevel.grid(row=2, column=3)

    def getallergy(self):
        ingred = self.ingred
        self.allergyinfo = ingred.get()   
        #print self.allergyinfo
        alist = tk.Label(self.master, text="Allergens: " + self.allergyinfo , bg='#77BA9B')
        alist.grid(row=3, column=3)   

    def run(self):
        self.foodbuttons()
        self.words()
        self.danger()
        self.allergy()
        self.checkdanger()
        self.checkallergy()

infotext = """Please be safe. 
        We are not responsible for food poisioning, allergic reactions, broken blenders, gross recipes or anything else.  
        A CricketHoneyKale creation by Lucy Wilcox, Lisa Hachmann, and Logan Sweet. 
        Please direct all negative feedback to byron.wasti@students.olin.edu"""

root = tk.Tk()
app = Application(root)
app.master.title('CricketHoneyKale')
root.configure(bg='#77BA9B')
root.mainloop()
