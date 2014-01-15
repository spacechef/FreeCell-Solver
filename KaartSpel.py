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

    def voeg_toe(self, kaart):
        self.kaartspel.append(kaart)

    def schud(self):
        shuffle(self.kaartspel)