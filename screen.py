# -*- coding: utf-8 -*-
from Tkinter import Tk, Canvas

class Screen(Canvas):
    """
    Ecran de visualisation : grille + signaux

   """
    def __init__(self, parent=None, width=800, height=800, background="white"):
        """
        Initialisation

        parent : le parent dans l'application
        width,height : dimension de l'ecran
        background : fond d'ecran

        signal_X, ... : identifiants des signaux 
        color_X, ... : couleur d'affichage des siganux
        """
        Canvas.__init__(self)
        self.parent = parent

        self.lines = []

        self.width = width
        self.height = height

        self.signal_X = None
        self.color_X = "red"

        self.configure(bg=background, bd=2, relief="sunken")
        self.bind("<Configure>", self.resize)

    def resize(self, event):
        """
        En cas de reconfiguration de fenetre
        """
        print("Screen.resize()")
        if event:
            for line in self.lines:
                self.delete(line)
            self.width = event.width
            self.height = event.height
            self.draw_grid()

    def draw_grid(self, nX=10, nY=10):
        """
        Representation des carreaux de la grille

        nX : pas horizontal
        nY : pas vertical
        """
        print("Screen.draw_grid('%d','%d')" % (nX, nY))

        self.lines = []

        "Repere d'affichage"
        self.lines.append( self.create_line(10, self.height/2, self.width, self.height/2, arrow="last") )
        self.lines.append( self.create_line(10, self.height-5, 10, 5, arrow="last") )

        pasWidth = self.width / nX
        pasHeight = self.height /nY
        for t in range(1, nX+1):
            self.lines.append( self.create_line(t*pasWidth, self.height, t*pasWidth, -self.height) )
            self.lines.append( self.create_line(0, t*pasHeight, self.width, t*pasHeight) )
        return

    def plot_signal(self, name, signal=None):
        """
        Affichage de signal

        name : nom du signal ("X","Y","X-Y")
        signal : liste des couples (temps,elongation) ou (elongation X, elongation Y)
        """
        if signal and len(signal) > 1:
            if name == "X":
                if self.signal_X > -1:
                    self.delete(self.signal_X)
                plot = [(x*self.width, y*self.height + self.height/2) for (x, y) in signal]
                self.signal_X = self.create_line(plot, fill=self.color_X, smooth=1, width=3)

if __name__ == "__main__":
    root = Tk()
    screen = Screen(root)
    screen
    root.mainloop()
