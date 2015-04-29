import Tkinter as tk


class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()  
        self.master = master
        
        self.w()
    	self.box()


    def w(self):
    	disclaimer = tk.Label(self.master, text = "\n\nPlease be safe. \n We are not responsible for food poisioning, allergic reactions, broken blenders, gross recipes or anything else.")
        disclaimer.grid(row=5,column=0,columnspan=4, pady=10)

    def box(self):     

        #self.value = " abc"
        value = tk.StringVar()

        dangerbox = tk.Spinbox(self.master,textvariable=value,from_=0, to=5)
        dangerbox.grid(row=0, column=2)

        but = tk.Button(self.master, text='get dangerous',command=self.obtener)
        but.grid(row=0, column=3, padx=20, pady=30)

        #return value.get()
        #self.value = value
        #self.value = value.get()
        #value.get() = self.value
        self.value = value
   
    def obtener(self):
    #def obtener(self):
    	#print self.value
    	value =
    	print value.get()

root = tk.Tk()
app = Application(root)
app.master.title('I hope this works')
root.mainloop()