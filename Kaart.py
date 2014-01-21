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

    def kan_naar_freecel(self, freecel):
            if freecel.nummer == 0 and freecel.soort == 'L':
                return True
            else:
                return False
    
    def kan_naar_een_lege_kolom(self, bord):
        for kolom in bord.kolommen:
            if len(kolom.kaarten) == 0:
                return True

    def voeg_toe_aan_doelcel(self, bord):
        kolom_en_kaart = bord.vind_kolom_en_kaart(self)
        for doelcel in bord.doelcellen:
            if self.nummer == doelcel.kaarten[-1].nummer + 1 and self.soort == doelcel.kaarten[-1].soort:
                doelcel.voeg_toe(self)
                break
            elif doelcel.kaarten[-1].nummer == 0 and doelcel.kaarten[-1].soort == 'L':      
                doelcel.voeg_toe(self)
                break

    def voeg_toe_aan_freecel(self, bord):
        teller = 0
        for freecell in bord.freecells:
            if freecell.nummer == 0 and freecell.soort == 'L':
                bord.freecells[teller] = self
                return True
            else:
                teller += 1
        
        for kolom in bord.kolommen:
            if len(kolom.kaarten) == 0:
                kolom.voeg_toe(self)
                return True
    
    def kan_naar_een_kolom(self, kolommen):
        for kolom in kolommen:
            if len(kolom.kaarten) > 0:
                if self.soort != 'L':
                    if self.nummer == kolom.kaarten[-1].nummer - 1 and self.geef_kleur() != kolom.kaarten[-1].geef_kleur():
                        return True
            
    def verplaats_naar_een_kolom(self, bord): # deze moet nogmaals gechecked worden
        kolom_en_kaart = bord.vind_kolom_en_kaart(self)
        if self.is_freecell(bord):
            for kolom in bord.kolommen:
                if len(kolom.kaarten) > 0:
                    if self.nummer == kolom.kaarten[-1].nummer - 1 and self.geef_kleur() != kolom.kaarten[-1].geef_kleur():
                        kolom.voeg_toe(self)
                        break
        else:
            for kolom in bord.kolommen:
                if kolom != kolom_en_kaart[0]:
                    if len(kolom.kaarten) > 0:
                        if self.nummer == kolom.kaarten[-1].nummer - 1 and self.geef_kleur() != kolom.kaarten[-1].geef_kleur():
                            kolom.voeg_toe(self)
                            break
    
    def diepte(self, bord):
        kolom_en_kaart = bord.vind_kolom_en_kaart(self)
        index_nummer_kaart = kolom_en_kaart[0].kaarten.index(self)
        lengte_kolom = len(kolom_en_kaart[0].kaarten)
        aantal_bovenliggende_kaarten = lengte_kolom - index_nummer_kaart - 1
        return aantal_bovenliggende_kaarten
    
    def is_freecell(self, bord):
        for kaart in bord.freecells:
            if kaart.nummer == self.nummer and kaart.soort == self.soort:
                return True                      
    
    def is_direct_speelbaar(self, bord):
        for kolom in bord.kolommen:
            if len(kolom.kaarten) > 0:
                if self is kolom.kaarten[-1]:
                    return True