from Kolom import Kolom
'''
Created on 8 Jan 2014

@author: spacechef
'''

class Kaart(object):

    def __init__(self, nummer, soort):
        self.nummer = nummer
        self.soort = soort

    #geeft de kleur van de kaart terug
    def geef_kleur(self):
        if self.soort == "R" or self.soort == "H":
            return "rood"
        else:
            return "zwart"

    #kijkt of een kaart naar een doelcel kan
    def kan_naar_een_doelcel(self, doelcellen):
        for doelcel in doelcellen:
            if self.nummer == doelcel.kaarten[-1].nummer + 1 and self.soort == doelcel.kaarten[-1].soort:
                return True
            elif self.nummer == doelcel.kaarten[-1].nummer + 1 and doelcel.kaarten[-1].soort == 'L':
                return True
    
    #kijkt of een kaart naar een freecell kan
    def kan_naar_freecel(self, freecel):
            if freecel.nummer == 0 and freecel.soort == 'L':
                return True
            else:
                return False
    
    #kijkt of een kaart naar een andere kolom kan
    def kan_naar_een_kolom(self, bord):
        kolom_en_kaart = bord.vind_kolom_en_kaart(self)
        for kolom in bord.kolommen:
            if kolom.aantal > 0: #controleert of er kaarten in de kolom zitten om index errors te voorkomen
                if kolom_en_kaart is None or kolom != kolom_en_kaart[0]: #zorgt ervoor dat de kaart niet bovenop zijn eigen kolom geplaats kan worden
                    if self.soort != 'L': #controleert of de kaart niet een lege kaart is (0, 'L')
                        if self.nummer == kolom.kaarten[-1].nummer - 1 and self.geef_kleur() != kolom.kaarten[-1].geef_kleur():
                            return True
    
    #bepaalt het aantal kaarten dat bovenop de huidige kaart ligt en geeft het aantal terug
    def diepte(self, bord):
        kolom_en_kaart = bord.vind_kolom_en_kaart(self)
        index_nummer_kaart = kolom_en_kaart[0].kaarten.index(self)
        lengte_kolom = kolom_en_kaart[0].aantal
        aantal_bovenliggende_kaarten = lengte_kolom - index_nummer_kaart - 1
        return aantal_bovenliggende_kaarten
    
    #kijkt of een de kaart een freecellkaart is
    def is_freecell(self, bord):
        for kaart in bord.freecells:
            if kaart.nummer == self.nummer and kaart.soort == self.soort:
                return True                      
    
    #kijkt of een kaart direct speelbaar is (bovenop ligt zonder andere kaarten te bewegen)
    def is_direct_speelbaar(self, bord):
        for kolom in bord.kolommen:
            if len(kolom.kaarten) > 0:
                if self is kolom.kaarten[-1]:
                    return True