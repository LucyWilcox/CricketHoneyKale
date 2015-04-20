#!/usr/bin/env python3
import Tkinter as tk  
from salad import *
 
class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()  
        #self.master = master
        #self.button_grid.grid()
        
        self.createWidgets()
        self.placeWidgets()
 
    def createWidgets(self):
        tk.Label(self.master, text="First").grid(row=0)
        tk.Label(self.master, text="Second").grid(row=1)
        tk.Label(self.master, text= "logan").grid()

        e1 = tk.Entry(self.master)
        e2 = tk.Entry(self.master)

        salad = tk.Button( XXXXXXXX , text = 'Generate me a salad!',command = lambda:self.display_recipe('salad'))

        # feedback.grid(row=1, column=1)
        # title.grid(row=1, column=1)
        # quit.grid(row=1, column=1)
        # soup.grid(row=1, column=1)
        salad.grid(row=1, column=1)
        # smoothie.grid(row=1, column=1)
        # danger.grid(row=1, column=1)
        # disclaimer.grid(row=1, column=1)


    def placeWidgets(createWidgets):
        pass
        
root = tk.Tk()
app = Application(root)
app.master.title('I hope this works')
root.mainloop()




# import Tkinter
# root = Tkinter.Tk(  )
# for r in range(3):
#     for c in range(4):
#         Tkinter.Label(root, text='R%s/C%s'%(r,c),borderwidth=1 ).grid(row=r,column=c)
# root.mainloop(  )