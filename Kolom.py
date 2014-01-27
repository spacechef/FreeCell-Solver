'''
Created on 8 Jan 2014

@author: spacechef
'''

class Kolom(object):

    def __init__(self):
        self.kaarten = []
        self.aantal = 0
    
    #voegt aan kaart toe aan zichzelf
    def voeg_toe(self, kaart):
        self.kaarten.append(kaart)
        self.aantal += 1
    
    #verwijdert de meegegeven kaart uit de kolom en past self.aantal aan
    def verwijder(self, te_verwijderen_kaart):
        for kaart in self.kaarten:
            if kaart.nummer == te_verwijderen_kaart.nummer and kaart.soort == te_verwijderen_kaart.soort:
                self.kaarten.remove(kaart)
                self.aantal -= 1
                return True