from Tkinter import Tk, Frame, Menubutton, Menu

import pickle
import tkMessageBox
from tkFileDialog import *

class MenuBar(Frame):
	def __init__(self, parent=None):
		Frame.__init__(self, borderwidth=2)
		self.parent = parent

		mbuttonFile = Menubutton(self, text="Fichier")
		mbuttonPlus = Menubutton(self, text="Plus")
		mbuttonQuit = Menubutton(self, text="Quitter")
		
		mbuttonFile.pack(side="left")
		mbuttonPlus.pack(side="left")
		mbuttonQuit.pack(side="left")

		menuFile = Menu(mbuttonFile)
		menuFile.add_command(label="Enregistrer Default", command=self.defaultSave)
		menuFile.add_command(label="Enregistrer", command=self.save)
		menuFile.add_command(label="Charger Default", command=self.defaultLoad)
		menuFile.add_command(label="Charger Choix", command=self.load)


		menuPlus = Menu(mbuttonPlus)
		menuPlus.add_command(label="Infos")

		menuQuit = Menu(mbuttonQuit)
		menuQuit.add_command(label="Quitter", command=parent.quit)
		menuQuit.add_command(label="Quitter avec confirmation", command=self.confirmQuit)

		mbuttonFile.configure(menu=menuFile)
		mbuttonPlus.configure(menu=menuPlus)
		mbuttonQuit.configure(menu=menuQuit)

	def defaultSave(self):
		with open('./Sauvegardes/Default', 'wb') as fichier:
			save_pickler = pickle.Pickler(fichier)
			save_pickler.dump(self.getParameters())

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

	def save(self):
		
		fichier = asksaveasfile(mode='wb')
		save_pickler = pickle.Pickler(fichier)
		save_pickler.dump(self.getParameters())

	def getParameters(self):
		parameters = {
			"amplitude" : self.parent.control_X.scale_A.get(),
			"frequence" : self.parent.control_X.scale_F.get(),
			"phase" : self.parent.control_X.scale_P.get(),
			"time" : self.parent.control_time.scale_time.get()
		}
		return parameters

	def confirmQuit(self):
	    result = tkMessageBox.askquestion("Quit", "Are You Sure?", icon='warning')
	    if result == 'yes':
	        self.parent.quit()
	    else:
	        print "Then we don't quit !"

if __name__ == "__main__":
    root = Tk()
    menuBar = MenuBar(root)
    menuBar.pack()
    root.mainloop()