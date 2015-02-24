from Tkinter import Tk, Frame, Menubutton, Menu

import pickle
from tkFileDialog import *

class MenuBar(Frame):
	def __init__(self, parent=None):
		Frame.__init__(self, borderwidth=2)
		self.parent = parent

		mbuttonFile = Menubutton(self, text="Fichier")
		mbuttonFile.pack()

		menuFile = Menu(mbuttonFile)
		menuFile.add_command(label="Enregistrer Default", command=self.defaultSave)
		menuFile.add_command(label="Charger Default", command=self.defaultLoad)
		menuFile.add_command(label="Charger Choix", command=self.load)
		menuFile.add_command(label="Quitter sans Enregistrer", command=parent.quit)

		mbuttonFile.configure(menu=menuFile)

	def defaultSave(self):
		parameters = {
			"amplitude" : self.parent.control_X.scale_A.get(),
			"frequence" : self.parent.control_X.scale_F.get(),
			"phase" : self.parent.control_X.scale_P.get(),
			"time" : self.parent.control_time.scale_time.get()
		}
		with open('./Sauvegardes/Default', 'wb') as fichier:
			save_pickler = pickle.Pickler(fichier)
			save_pickler.dump(parameters)

	def defaultLoad(self):
		with open('./Sauvegardes/Default', 'rb') as fichier:
			mon_depickler = pickle.Unpickler(fichier)
			parameters = mon_depickler.load()
			self.parent.control_X.scale_A.set(parameters["amplitude"])
			self.parent.control_X.scale_F.set(parameters["frequence"])
			self.parent.control_X.scale_P.set(parameters["phase"])
			self.parent.control_time.scale_time.set(parameters["time"])
			self.parent.control_X.scale_P.update_signal()

	def load(self):
		fichier = askopenfile(mode='rb')
		mon_depickler = pickle.Unpickler(fichier)
		parameters = mon_depickler.load()
		self.parent.control_X.scale_A.set(parameters["amplitude"])
		self.parent.control_X.scale_F.set(parameters["frequence"])
		self.parent.control_X.scale_P.set(parameters["phase"])
		self.parent.control_time.scale_time.set(parameters["time"])
		self.parent.control_X.scale_P.update_signal()

if __name__ == "__main__":
    root = Tk()
    menuBar = MenuBar(root)
    menuBar.pack()
    root.mainloop()