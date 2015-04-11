import Tkinter as tk
import tkMessageBox 
class Application(tk.Frame): 
	def __init__(self, master=None):
		tk.Frame.__init__(self, master) 
		self.grid() 
		self.Error_popup_message()
	"""Commented code from making buttons"""
	#	self.createWidgets()
	# def createWidgets(self):
	# 	self.quitButton = tk.Button(self, text='Quit',command=self.quit) 
	# 	self.quitButton.grid() 
	"""Commented code to have an error button show up with a certain else-
	do not delete"""
	# def Error_popup_message(self):
 #   		tkMessageBox.showinfo("Recipe Generator", "No recipes found, try again")
app = Application() 
app.mainloop() 