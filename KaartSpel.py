from Kaart import Kaart
from random import shuffle
from sys import argv

class KaartSpel(object):

    def __init__(self):
        self.kaartspel = []
        self.seed = None
    
    #officieele freecell deel functie (code aangepast zodat het in ons programma werkt)
    def randomGenerator(self, seed=1):
        max_int32 = (1 << 31) - 1
        seed = seed & max_int32
 
        while True:
            seed = (seed * 214013 + 2531011) & max_int32
            yield seed >> 16
    
    def deal(self, seed):
        nc = 52
        cards = range(nc - 1, -1, -1)
        rnd = self.randomGenerator(seed)
        for i, r in zip(range(nc), rnd):
            j = (nc - 1) - r % (nc - i)
            cards[i], cards[j] = cards[j], cards[i]
        return cards

    def maak(self, seed):
        cards = self.deal(seed)
        seed = int(argv[1]) if len(argv) == 2 else 11982
        print "Hand", seed
        l = ["A23456789TJQK"[c / 4] + "KRHS"[c % 4] for c in cards]
        kaarten = []
        teller = 0
        for kaart in l:
            if l[teller][0] == 'A':
                self.voeg_toe(Kaart(1, l[teller][1]))
            elif l[teller][0] == 'T':
                self.voeg_toe(Kaart(10, l[teller][1]))
            elif l[teller][0] == 'J':
                self.voeg_toe(Kaart(11, l[teller][1]))
            elif l[teller][0] == 'Q':
                self.voeg_toe(Kaart(12, l[teller][1]))
            elif l[teller][0] == 'K':
                self.voeg_toe(Kaart(13, l[teller][1]))
            else: 
                self.voeg_toe(Kaart(int(l[teller][0]), l[teller][1]))
            teller += 1
            #einde van officiele freecell deel algoritme
    
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