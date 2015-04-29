import Tkinter as tk


class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()  
        self.master = master
        self.run()
        #self.placeWidgets()


    def danger(self):
    	disclaimer = tk.Label(self.master, text = "\n\nPlease be safe. \n We are not responsible for food poisioning, allergic reactions, broken blenders, gross recipes or anything else.")
        disclaimer.grid(row=5,column=0,columnspan=4, pady=10)


    def box(self):
    	quit = tk.Button(self.master, text='get dangerous',command=self.obtener)
        quit.grid(row=0, column=3, padx=20, pady=30)

        dangerbox = tk.Spinbox(self.master,textvariable=value,from_=0, to=5)
        dangerbox.grid(row=0, column=2)

    def obtener(self):
    	print value.get()



    def run(self):
    	self.danger()
    	self.box()
    	self.obtener()


root = tk.Tk()
app = Application(root)
app.master.title('I hope this works')
root.mainloop()