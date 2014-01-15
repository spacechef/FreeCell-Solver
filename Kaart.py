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

    def voeg_toe_aan_doelcel(self, doelcel):
            doelcel.voeg_toe(kaart)

    def voeg_toe_aan_freecel(self, kaart):
        teller = 0
        for freecell in self.freecells:
            if freecell.nummer == 0 and freecell.soort == 'L': #hier moet soortcheck bij
                self.freecells[teller] = kaart
            else:
                teller += 1