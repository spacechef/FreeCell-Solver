from Kolom import Kolom
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

    def voeg_toe_aan_doelcel(self, bord):
        kolom_en_kaart = bord.vind_kolom_en_kaart(self)
        for doelcel in bord.doelcellen:
            if self.nummer == doelcel.kaarten[-1].nummer + 1 and self.soort == doelcel.kaarten[-1].soort:
                doelcel.voeg_toe(self)
                kolom_en_kaart[0].verwijder_kaart(self)
                break
            elif doelcel.kaarten[-1].nummer == 0 and doelcel.kaarten[-1].soort == 'L':      
                kolom_en_kaart[0].verwijder(self)
                doelcel.voeg_toe(self)
                break

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
                return True
            else:
                return False
            
    def verplaats_naar_een_kolom(self, bord): # deze moet nogmaals gechecked worden
        kolom_en_kaart = bord.vind_kolom_en_kaart(self)
        for kolom in bord.kolommen:
            if len(kolom.kaarten) > 0 and kolom is not kolom_en_kaart[0]:
                if self.nummer == kolom.kaarten[-1].nummer - 1 and self.geef_kleur() is not kolom.kaarten[-1].geef_kleur():
                    kolom.voeg_toe(self)
                    kolom_en_kaart[0].verwijder_kaart(self)
                    
    
    def is_direct_speelbaar(self, bord):
        for kolom in bord.kolommen:
            if self is kolom.kaarten[-1]:
                return True
        
        for freecel in bord.freecells:
            if self is freecel:
                return True