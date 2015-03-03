# -*- coding: utf-8 -*-
from Tkinter import Tk, Frame, Menubutton, Menu, Toplevel, Button, Label

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
		menuPlus.add_command(label="Infos", command=self.showInfos)

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
			self.setParameters(parameters)

	def load(self):
		fichier = askopenfile(mode='rb')
		mon_depickler = pickle.Unpickler(fichier)
		parameters = mon_depickler.load()
		self.setParameters(parameters)

	def save(self):
		fichier = asksaveasfile(mode='wb')
		save_pickler = pickle.Pickler(fichier)
		save_pickler.dump(self.getParameters())

	def setParameters(self, parameters):
		self.parent.control_X.scale_A.set(parameters["amplitudeX"])
		self.parent.control_X.scale_F.set(parameters["frequenceX"])
		self.parent.control_X.scale_P.set(parameters["phaseX"])
		self.parent.control_Y.scale_A.set(parameters["amplitudeY"])
		self.parent.control_Y.scale_F.set(parameters["frequenceY"])
		self.parent.control_Y.scale_P.set(parameters["phaseY"])
		self.parent.control_time.scale_time.set(parameters["time"])
		self.parent.control_X.scale_P.update_signal()
		self.parent.control_Y.scale_P.update_signal()


	def getParameters(self):
		parameters = {
			"amplitudeX" : self.parent.control_X.scale_A.get(),
			"frequenceX" : self.parent.control_X.scale_F.get(),
			"phaseX" : self.parent.control_X.scale_P.get(),
			"amplitudeY" : self.parent.control_Y.scale_A.get(),
			"frequenceY" : self.parent.control_Y.scale_F.get(),
			"phaseY" : self.parent.control_Y.scale_P.get(),
			"time" : self.parent.control_time.scale_time.get()
		}
		return parameters

	def confirmQuit(self):
	    result = tkMessageBox.askquestion("Quit", "Are You Sure?", icon='warning')
	    if result == 'yes':
	        self.parent.quit()
	    else:
	        print "Then we don't quit !"

	def showInfos(self):
		top = Toplevel(bg="green")
		top.title("Infos")
		Label(top, text="Email maaath29").grid(row=1)
		Label(top, text="Développeur : ALLAIN Mathieu").grid(row=0)
		Button(top, text="Fermer", command=top.destroy).grid(row=2)

if __name__ == "__main__":
    root = Tk()
    menuBar = MenuBar(root)
    menuBar.pack()
    root.mainloop()