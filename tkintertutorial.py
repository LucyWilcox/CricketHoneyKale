from Tkinter import *
import tkMessageBox 
class Application(Frame): 
	def __init__(self, master):
		self.master = master
		self.page_frame = Frame(self.master, width = 500, height = 400, colormap = 'new')
		self.page_frame.pack_propagate(0) 
	#	self.next_frame = Frame(self.master, width = 500, height = 300, colormap = 'new')
		self.Opening_Page()
		self.page_frame.pack(fill = X)

	# """Uncomment to create the error popup message at startup"""
	# #	self.Error_popup_message()
	# """Commented code from making buttons"""

	def Opening_Page(self):
	 	Button(self.page_frame, text='Salad', justify =LEFT).pack(fill = BOTH, expand = 1)#,command=self.Next_Page()).pack(fill = X)
	 	Button(self.page_frame, text= 'Soup').pack(fill = X, expand = 1)
	 	Button(self.page_frame, text= "Smoothie").pack(fill = X, expand = 1)
	 	Button(self.page_frame, text = "Info").pack(fill = X, expand = 1)
	 	Button(self.page_frame, text='Quit',command=quit).pack(fill = BOTH, expand = 1) 
	"""Commented code to have an error button show up with a certain else-
	do not delete"""
	# def Next_Page(self):
	# 	Button(self.next_frame, text = 'Try Again', command = quit).pack(fill = X)

	#def Error_popup_message(self):
 #   		tkMessageBox.showinfo("Recipe Generator", "No recipes found, try again")

if __name__ == '__main__':
	root = Tk()
	app = Application(root) 
	root.mainloop() 