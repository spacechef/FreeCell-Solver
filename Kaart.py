'''
Created on 8 Jan 2014

@author: spacechef
'''

class Kaart(object):

    def __init__(self, nummer, soort):
        self.nummer = nummer
        self.soort = soort

    def geef_kleur(self):
        if self.soort == "R" or self.soort == "H":
            return "rood"
        else:
            return "zwart"

    def is_kleur(self, kleur):
        if self.geef_kleur == kleur:
            return True
        else:
            return False
    
    def kan_naar_een_doelcel(self, doelcellen):
        for doelcel in doelcellen:
            if self.nummer == doelcel.kaarten[-1].nummer + 1 and self.soort == doelcel.kaarten[-1].soort:
                return True
            elif self.nummer == doelcel.kaarten[-1].nummer + 1 and doelcel.kaarten[-1].soort == 'L':
                return True
            else:
                return False

    def kan_naar_freecel(self, freecel):
            if freecel.nummer == 0 and freecel.soort == 'L':
                return True
            else:
                return False

    def voeg_toe_aan_doelcel(self, doelcellen):
        for doelcel in doelcellen:
            if self.nummer == doelcel.kaarten[-1].nummer + 1 and self.soort == doelcel.kaarten[-1].soort:
                doelcel.voeg_toe(self)
            elif doelcel.kaarten[-1].nummer == 0 and doelcel.kaarten[-1].soort == 'L':
                doelcel.voeg_toe(self)

    def voeg_toe_aan_freecel(self, kaart):
        teller = 0
        for freecell in self.freecells:
            if freecell.nummer == 0 and freecell.soort == 'L': #hier moet soortcheck bij
                self.freecells[teller] = kaart
            else:
                teller += 1
    
    def kan_naar_een_kolom(self, kolommen):
        for kolom in kolommen:
            if self.nummer == kolom.kaarten[-1].nummer - 1 and self.geef_kleur() != kolom.kaarten[-1].geef_kleur():
                print self.nummer, self.soort
                return True
            else:
                return False
            
    def verplaats_naar_een_kolom(self, kolommen): # deze moet nogmaals gechecked worden
        for kolom in kolommen:
            if self.nummer == kolom.kaarten[-1].nummer - 1 and self.geef_kleur() is not kolom.kaarten[-1].geef_kleur():
                kolom.voeg_toe(self)
                start_kolom.verwijder_kaart(self)
    
    def vind_kaart(self):
        start_kolom = None
        for kolom in kolommen:
            if self is kolom.kaarten[-1]:
                start_kolom = kolom


    
    def is_direct_speelbaar(self, bord):
        for kolom in bord.kolommen:
            if self is kolom.kaarten[-1]:
                return True
        
        for freecel in bord.freecells:
            if self is freecel:
                return True