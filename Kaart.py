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