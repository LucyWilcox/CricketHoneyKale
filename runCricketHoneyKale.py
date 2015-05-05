import Tkinter as tk  
from main import *

class Application(tk.Frame):
    def __init__(self, master=None):
        """
        Creates the top leve (parent) TKinter frame and sets up the grid method of widget placement. 
        Defined minimum window size.
        Executes the function run, which conmtains all functions that need to be executed to run program. 
        """
        tk.Frame.__init__(self, master)
        self.grid()  
        self.master = master
        master.minsize(width=850, height=300)
        self.run()

    def foodbuttons(self):
        """
        Initializes and places buttons that create recipes. 
        self.display_recipe('foodname') feeds the desired recipe type to the dispay recipe function. 
        """
        soup = tk.Button(self.master, text = 'Generate me a soup!', command = lambda:self.display_recipe('soup'),bg=a, fg=d, activebackground=b, font= fo)
        salad = tk.Button(self.master, text = 'Generate me a salad!', command = lambda:self.display_recipe('salad'),bg=a, fg=d, activebackground=b, font= fo)
        smoothie = tk.Button(self.master, text = 'Generate me a smoothie!', command = lambda:self.display_recipe('smoothie'),bg=a, fg=d, activebackground=b, font= fo)
        sandwich = tk.Button(self.master, text = 'Generate me a sandwich!', command = lambda:self.display_recipe('sandwich'),bg=a, fg=d, activebackground=b, font= fo)

        soup.grid(row=1,column=0, padx=20)
        salad.grid(row=1,column=1, padx=20)
        smoothie.grid(row=1,column=2, padx=20)
        sandwich.grid(row=1,column=3, padx=20)

    def words(self):
        """
        Initializes and places the title, quit button, and info button. 
        Info button initializes pressinfo function. 
        """
        title = tk.Label(self.master, text = "Let's Cook Something!!", bg=c,fg=d, font= (fo,18))
        info = tk.Button(self.master, text="Information", command = self.pressinfo,bg=a, fg=d, activebackground=b, font= fo)
        quit = tk.Button(self.master, text='Quit',command=self.quit,bg=a, fg=d, activebackground=b, font= fo)

        title.grid(row=0, column=1, padx=20, columnspan=2)
        info.grid(row=0, column=0)
        quit.grid(row=0, column=3, padx=20, pady=30)

    def pressinfo(self):
        """
        Runs when info button is pressed. 
        Creates a new window named "top" that diplays infotext(deifned at bottom)
        """
        top = tk.Toplevel(bg=c)
        top.title("Information")
        disc = tk.Label(top, text = infotext , font= fo, bg=c)
        disc.grid()
          
    def display_recipe(self, want_to_cook):
        """
        Initialized when a recipe button is pressed. 
        Uses make_recipe from main. 
        Uses inputs: 
            want_to_cook (the type of food you want)
            self.allergyinfo (comes from checkallergy)
            self.dangervalue (comes from checkdanger)
        """
        recipe_directions = make_recipe(want_to_cook, self.allergyinfo, self.dangervalue)
        top = tk.Toplevel(bg=c)
        top.title("Recipe")
        top.resizable(0,0)
        rec = tk.Label(top, text = recipe_directions , font= fo, bg=c)
        rec.grid(row=2,column=1, pady=35, padx=35)

    def danger(self):   
        """
        Initializes and places danger text instructions and selsction spinbox.
        Assigns the number recorded in the spinbox to the variable value, 
            which is then made assigned to an attribute of self as self.value. 
        """  
        value = tk.StringVar()
        dangerdescript = tk.Label(self.master, text="How dangerous are you? " ,fg=d, bg=c, font= fo)
        dangerdescript.grid(row=2, column=0)
        dang = tk.Spinbox(self.master,textvariable=value,from_=0, to=5, width = 3,fg=d, font= (fo,15))
        dang.grid(row=2, column=1)
        but = tk.Button(self.master, text='Get Dangerous',command=self.getdanger,bg=a, fg=d, activebackground=b, font= fo)
        but.grid(row=2, column=2, padx=20, pady=30)
        self.value = value
 
    def allergy(self): 
        """
        Initializes and places allergy text instructions and entry box.
        Assigns the number recorded in the box to the variable ingred, 
            which is then made assigned to an attribute of self as self.ingred. 
        """
        ingred = tk.StringVar()
        allerdescript = tk.Label(self.master, text="What are you allergic to?\n(seperated by commas)", bg=c,fg=d, font= fo)
        allerdescript.grid(row=3, column=0)
        aller = tk.Entry(self.master, textvariable=ingred)
        aller.grid(row=3, column=1)
        butt = tk.Button(self.master, text='Record Allergens', command=self.getallergy,bg=a, fg=d, activebackground=b, font= fo)
        butt.grid(row=3,column=2)
        self.ingred = ingred

    def getdanger(self):
        """
        Takes self.value and reassigns it to value. 
        Uses the TKinter .get() function to get the info from this entry and 
            assign it to self.dangervalue, which is then used in display_recipe
        Also initialized and displays an updated danger level value.
        """
        value = self.value
        self.dangervalue = value.get()
        dlevel = tk.Label(self.master, text="Current danger level is " + self.dangervalue , bg=c, font= fo)
        dlevel.grid(row=2, column=3)

    def getallergy(self):
        """
        Takes self.ingred and reassigns it to ingred. 
        Uses the TKinter .get() function to get the info from this entry and 
            assign it to self.allergyinfo, which is then used in display_recipe. 
        """
        ingred = self.ingred
        self.allergyinfo = ingred.get()   

    def checkdanger(self):
        """
        If there is no value assigned to self.dangervalue, assigns it the value 0 (no danger)
        This gives display_recipe a value even if the user does not press "Get Dangerous"
        """
        if hasattr(self, "dangervalue"):
            pass
        else:
            self.dangervalue = 0

    def checkallergy(self):
        """
        If there is no value assigned to self.allergyvalue, assigns it an empty string (no allergens)
        This gives display_recipe a value even if the user does not press "Record Allergens"
        """
        if hasattr(self, "allergyvalue"):
            pass
        else:
            self.allergyinfo = " "

    def run(self):
        """
        The contains all the functions that need ot be run to execute the program and create the GUI.
        This runs when init runs. They could be pasted there, but this keeps the init function clean and relatively empty. 
        """
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

fo = "Dingbats" # font style
a = '#0f9fb4'   # button color      (Alternate color schemes avaliable at bottom)
b = '#0fb493'   # button hover
c = '#c9e1c1'   # big background
d = '#152737'   # font color

root = tk.Tk()
app = Application(root)
app.master.title('CricketHoneyKale')
root.configure(bg=c)
root.mainloop()



######################################################################################
############################Alternate Color Palettes Here#############################
######################################################################################

# a = '#639BF1'   # button color
# b = '#3B5998'   # button hover
# c = '#77BA9B'   # big background
# d = '#0101DF'   # font color

# a = '#f9f1b5'   # button color
# b = '#a6d8de'   # button hover
# c = '#dddad6'   # big background
# d = '#2E2E2E'   # font color