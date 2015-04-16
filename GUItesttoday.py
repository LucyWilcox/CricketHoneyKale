#!/usr/bin/env python3
import Tkinter as tk  
 
class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()  
        self.createWidgets()
        self.placeWidgets()
 
    def createWidgets(self):
        self.quitButton = tk.Button(self, text='Quit',command=self.quit)
        self.quitButton.grid()

    def placeWidgets(createWidgets):
    	pass
    	
 
app = Application()
app.master.title('I hope this works')
app.mainloop()




# import Tkinter
# root = Tkinter.Tk(  )
# for r in range(3):
#     for c in range(4):
#         Tkinter.Label(root, text='R%s/C%s'%(r,c),borderwidth=1 ).grid(row=r,column=c)
# root.mainloop(  )