from Kaart import Kaart
from random import shuffle

class KaartSpel(object):

    def __init__(self):
        self.kaartspel = []

    def maak(self):
        for i in range(1,14):
            kaart = Kaart(i, "R")
            self.voeg_toe(kaart)
        for i in range(1,14):
            kaart = Kaart(i, "H")
            self.voeg_toe(kaart)
        for i in range(1,14):
            kaart = Kaart(i, "S")
            self.voeg_toe(kaart)
        for i in range(1,14):
            kaart = Kaart(i, "K")
            self.voeg_toe(kaart)
            
    def maak_oplosbaar_spel(self):
        self.voeg_toe(Kaart(7, "R"))
        self.voeg_toe(Kaart(7, "H"))
        self.voeg_toe(Kaart(7, "S"))
        self.voeg_toe(Kaart(7, "K"))
        self.voeg_toe(Kaart(6, "R"))
        self.voeg_toe(Kaart(6, "H"))
        self.voeg_toe(Kaart(6, "S"))
        self.voeg_toe(Kaart(6, "K"))
        self.voeg_toe(Kaart(5, "R"))
        self.voeg_toe(Kaart(5, "H"))
        self.voeg_toe(Kaart(5, "S"))
        self.voeg_toe(Kaart(5, "K"))
        self.voeg_toe(Kaart(4, "R"))
        self.voeg_toe(Kaart(4, "H"))
        self.voeg_toe(Kaart(4, "S"))
        self.voeg_toe(Kaart(4, "K"))
        self.voeg_toe(Kaart(3, "R"))
        self.voeg_toe(Kaart(3, "H"))
        self.voeg_toe(Kaart(3, "S"))
        self.voeg_toe(Kaart(3, "K"))
        self.voeg_toe(Kaart(2, "R"))
        self.voeg_toe(Kaart(2, "H"))
        self.voeg_toe(Kaart(2, "S"))
        self.voeg_toe(Kaart(2, "K"))
        self.voeg_toe(Kaart(1, "R"))
        self.voeg_toe(Kaart(1, "H"))
        self.voeg_toe(Kaart(1, "S"))
        self.voeg_toe(Kaart(1, "K"))

        
    #voegt een kaart toe aan zichzelf
    def voeg_toe(self, kaart):
        self.kaartspel.append(kaart)
    
    #schud de kaarten in self.kaartspel
    def schud(self):
        shuffle(self.kaartspel)