from Tkinter import *
import tkMessageBox 
class Application(Frame): 
	def __init__(self, master):
		self.master = master
		self.page_frame = Frame(self.master, width = 1000, height = 1000, colormap = 'new')
		self.Opening_Page()
		self.page_frame.pack(fill = X)

	# """Uncomment to create the error popup message at startup"""
	# #	self.Error_popup_message()
	# """Commented code from making buttons"""

	def Opening_Page(self):
	 	Button(self.page_frame, text='Salad').pack(fill = X)#,command=self.Next_Page()) 
	 	Button(self.page_frame, text='Quit',command=quit).pack(fill = X) 

	"""Commented code to have an error button show up with a certain else-
	do not delete"""
	# def Next_Page(self):
	# #	self.nextbutton = tk.Button(self, text = 'Next')
	# 	self.page_frame = Frame(self.master)
	# def Error_popup_message(self):
 #   		tkMessageBox.showinfo("Recipe Generator", "No recipes found, try again")

if __name__ == '__main__':
	root = Tk()
	app = Application(root) 
	root.mainloop() 