# -*- coding: utf-8 -*-
from Tkinter import Tk, Frame, Checkbutton, IntVar

class SignalSelected(Frame):
    """
    Selection signal : Y, X ou XY

   """
    def __init__(self, parent):
        Frame.__init__(self)
        self.configure(bd=1, relief="sunken")
        self.parent = parent

        #Choix affichage X, Y ou XY
        self.X = IntVar()
        self.Y = IntVar()
        self.XY = IntVar()

        self.XCheckBox = Checkbutton(self, text="Courbe X", command=self.updateX, variable=self.X,
            onvalue = 1, offvalue = 0, height=5,
            width = 20)

        self.YCheckBox = Checkbutton(self, text="Courbe Y", onvalue = 1, offvalue = 0, 
            variable=self.Y, height=5,
            width = 20, command=self.updateY)

        self.XYCheckBox = Checkbutton(self, text="Courbe XY", onvalue = 1, offvalue = 0, 
            variable=self.XY, height=5,
            width = 20, command=self.updateXY)

        self.XCheckBox.select()
        self.YCheckBox.select()
        
        self.XCheckBox.pack(fill="both", expand="yes")
        self.YCheckBox.pack(fill="both", expand="yes")
        self.XYCheckBox.pack(fill="both", expand="yes")

    def updateX(self):
        if self.X.get():
            self.parent.view.signal_X_allowed = 1
            self.parent.control_X.update_signal(None)
        else:
            self.parent.view.signal_X_allowed = 0
            self.parent.view.delete( self.parent.view.signal_X)

    def updateY(self):
        if self.Y.get():
            self.parent.view.signal_Y_allowed = 1
            self.parent.control_Y.update_signal(None)
        else:
            self.parent.view.signal_Y_allowed = 0
            self.parent.view.delete( self.parent.view.signal_Y)

    def updateXY(self):
        if self.XY.get():
            self.parent.view.signal_XY_allowed = 1
            self.parent.view.plot_signal('X-Y')
        else:
            self.parent.view.signal_XY_allowed = 0
            self.parent.view.delete(self.parent.view.signal_XY)

if __name__ == "__main__": 
    root = Tk()
    SignalSelected(root).pack()
    root.mainloop()
