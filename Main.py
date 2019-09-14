import Tkinter as tk
import ttk

VERSION='0.0.01'

class Lexicon_App:

	def __init__(self):

		print 'app initialized'

	def create_window(self):

		self.window=tk.Tk()
		self.window.title('Lexicon manager version  ' + VERSION)

		self.win_width=self.window.winfo_width()

		self.menu=tk.Menu(self.window)

		filemenu=tk.Menu(self.menu)
		filemenu.add_command(label='save')
		filemenu.add_command(label='load')
		filemenu.add_command(label='export')
		self.menu.add_cascade(label='File',menu=filemenu)
		self.menu.add_command(label='roots')
		self.menu.add_command(label='compound')
		self.window.config(menu=self.menu)


		self.left_frame=tk.Frame(self.window,width=(150),bg='cyan')
		self.tools_frame=tk.Frame(self.left_frame,height=40,bg='brown')
		self.list_frame=tk.Frame(self.left_frame,height=420)
		self.main_frame=tk.Frame(self.window,width=(500),height=460)

		self.left_frame.pack(side=tk.LEFT,fill='y')
		self.left_frame.pack_propagate(0)
		self.tools_frame.pack(fill='x')
		self.tools_frame.pack_propagate(0)
		self.list_frame.pack(fill='x')
		self.list_frame.pack_propagate(0)
		self.main_frame.pack(side=tk.LEFT)
		self.main_frame.pack_propagate(0)

		self.tabs=ttk.Notebook(self.main_frame)
		self.derivation_tab=ttk.Frame(self.tabs)
		self.compound_tab=ttk.Frame(self.tabs)

		self.tabs.add(self.derivation_tab,text='derivations')
		self.tabs.add(self.compound_tab,text='compounds')

		self.tabs.pack(expand=1, fill='both')

		#pack_propagate(0)

		self.window.mainloop()

app= Lexicon_App()
app.create_window()
