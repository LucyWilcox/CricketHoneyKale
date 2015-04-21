"""
GUI for Cricket Honey Kale
"""

from Tkinter import *
from salad import *


class MakeWindow(Frame):
    """ """

    def __init__(self, master):
        """ Initializes the GUI. Creates a frame and then adds button from 
            add_button method"""
        # Initialize GUI & frame
        self.master = master
        self.button_frame = Frame(self.master)
        master.minsize(width = 500, height = 400)
        master.maxsize(width = 500, height = 400)
        self.add_button()
        self.instructions()
        self.button_frame.pack()
        # For calling premade bokeh graphs
        #self.current_directory = 'file://' + sys.argv[0]


    def add_button(self):
        """ Creates the buttons and entry form on the GUI. There are two portions to the
            GUI: buttons to look at common information of the data set, and buttons to
            compare your input to the data set."""
        # Quit Button
        Button(self.button_frame, text = 'Quit', command = quit).pack()
        # Common Information Buttons
        Label(self.button_frame, text = "\n\nLets eat something:").pack()
        
        saladbutt = Button(self.button_frame, text = 'Generate me a salad!',
                command = lambda:self.display_recipe('salad'))
        soupbutt = Button(self.button_frame, text = 'Generate me a soup!',
                command = lambda:self.display_recipe('soup'))
        smoothiebutt = Button(self.button_frame, text = 'Generate me a smoothie!',
                command = lambda:self.display_recipe('smoothie'))

        Label(self.button_frame, text = '\n\nHow Dangerous Are You?:').pack(fill = X)
        global selected_danger
        selected_danger = Entry(self.button_frame)
        selected_danger.pack(expand = 2)

        saladbutt.pack(expand = 2)
        soupbutt.pack(expand = 2)
        smoothiebutt.pack(expand = 2)
    
    def instructions(self):
        instruct = Label(self.button_frame, text = "\n\nPlease be safe. \n We are not responsible for food poisioning, allergic \n reactions, broken blenders, gross recipes or anything else.")
        instruct.pack(expand = 2)


    def display_recipe(self, want_to_cook):
        sel_danger = selected_danger.get()
        print sel_danger
        recipe_directions = make_recipe(want_to_cook, sel_danger)
        
        see = Label(self.button_frame, text = "\n" + recipe_directions).pack(fill=BOTH)

if __name__ == '__main__':
    root = Tk()
    ex = MakeWindow(root)
    root.resizable(width=FALSE, height=FALSE)
    root.mainloop() 
