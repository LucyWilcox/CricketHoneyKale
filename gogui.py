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
        self.button_frame = Frame(self.master, width = 400, height = 400, colormap = 'new')
        self.add_button()
        self.button_frame.pack(fill = X)
        # For calling premade bokeh graphs
        self.current_directory = 'file://' + sys.argv[0]


    def add_button(self):
        """ Creates the buttons and entry form on the GUI. There are two portions to the
            GUI: buttons to look at common information of the data set, and buttons to
            compare your input to the data set."""
        # Quit Button
        Button(self.button_frame, text = 'Quit', command = quit).pack(fill = X)
        # Common Information Buttons
        Label(self.button_frame, text = "\n\nLets eat something:").pack(fill = X)
        Button(self.button_frame, text = 'Generate me a salad!', 
            command = lambda:self.display_recipe('salad')).pack(fill = X)
        Button(self.button_frame, text = 'Generate me a soup!', 
            command = lambda:self.display_recipe('soup')).pack(fill = X)
        Button(self.button_frame, text = 'Generate me a smoothie!', 
            command = lambda:self.display_recipe('smoothie')).pack(fill = X)
        Label(self.button_frame, text = "\n\nPlease be safe. \n We are not responsible for food poisioning, allergic reactions, broken blenders, gross recipes or anything else.").pack(fill = X)
        # # Password Entry
        # Label(self.button_frame, text = '\n\nEnter a Password Below to Find Information:').pack(fill = X)
        # global entry_pw 
        # entry_pw = Entry(self.button_frame)
        # entry_pw.pack(fill = X)


    def display_recipe(self, want_to_cook):
        recipe_directions = make_recipe(want_to_cook)
        see = Label(self.button_frame, text = recipe_directions).pack(fill = X)

if __name__ == '__main__':
    root = Tk()
    ex = MakeWindow(root)
    root.mainloop() 