from Tkinter import Tk, Frame, Menubutton, Menu

import pickle

class MenuBar(Frame):
	def __init__(self, parent=None):
		Frame.__init__(self, borderwidth=2)
		mbuttonFile = Menubutton(self, text="Fichier")
		mbuttonFile.pack()

		menuFile = Menu(mbuttonFile)
		menuFile.add_command(label="Enregistrer Default", command=defaultSave)
		menuFile.add_command(label="Quitter sans Enregistrer", command=parent.quit)

		mbuttonFile.configure(menu=menuFile)

	def defaultSave(self):
		print(self.parent.control_X.scale_A.get())
		parameters = {
			"amplitude" : self.parent.control_X.scale_A.get(),
			"frequence" : self.parent.control_X.scale_F.get(),
			"phase" : self.parent.control_X.scale_P.get(),
			"time" : self.parent.control_time.scale_time.get()
		}
		with open('Sauvegardes/Default', 'rb') as fichier:
			save_pickler = pickle.Pickler(fichier)
			save_pickler.dump(parameters)

if __name__ == "__main__":
    root = Tk()
    menuBar = MenuBar(root)
    menuBar.pack()
    root.mainloop()