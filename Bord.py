from Kolom import Kolom
from Kaart import Kaart
'''
Created on 8 Jan 2014

@author: spacechef
'''

class Bord(object):
    '''
    classdocs
    '''


    def __init__(self):
        self.aantal_kolommen = 8
        self.kolommen = []
        self.aantal_freecells = 4
        self.freecells = []
        self.aantal_doelcellen = 4
        self.doelcellen = []

    #maakt de doel en freecellen
    def maak_doel_en_freecellen(self):
        for aantal_freecells in range(self.aantal_freecells):
            kaart = Kaart(0, 'L')
            self.freecells.append(kaart)

        for aantal_doelcellen in range(self.aantal_doelcellen):
            doelcel = Kolom()
            self.doelcellen.append(doelcel)
            doelcel.voeg_toe(Kaart(0,'L'))
    
    #maakt de kolommen voor de kaarten
    def maak_kolommen(self):
        for aantal_kolommen in range(self.aantal_kolommen):
            kolom = Kolom()
            self.kolommen.append(kolom)
    
    #deelt de kaarten over de kolomen eerste kaart eerste kolom 2de kaart 2de kolom 3de kaart 3de kolom etc 
    def deel_kaarten(self, kaartspel):
        teller = 0
        for kaart in kaartspel.kaartspel:
            if teller == 8:
                teller = 0
            self.kolommen[teller].voeg_toe(kaart)
            teller += 1
    
    #geeft het aantal freecells terug (incl een lege kolom omdat dit als een freecel beschouwd kan worden zolang er geen kaart op zit)
    def geef_aantal_freecells(self):
        aantal_freecells = 0
        for kaart in self.freecells:
            if kaart.nummer == 0:
                aantal_freecells += 1
        for kolom in self.kolommen:
            if kolom.aantal == 0:
                aantal_freecells += 1

        return aantal_freecells
    
    #geeft de kolom en de kaart van de gezochte kaart terug in een variabele
    def vind_kolom_en_kaart(self, gezochte_kaart):
        if gezochte_kaart is not None:
            for kolom in self.kolommen:
                for kaart in kolom.kaarten:
                    if gezochte_kaart == kaart:
                        return(kolom, kaart)
    
    #verwijdert een kaart uit een kolom waar hij inzat voordat deze verplaatst is (zodat een kaart niet gedupliceerd kan worden)
    def verwijder(self, te_verwijderen_kaart, vorige_kolom):
        for kolom in self.kolommen:
            if kolom == vorige_kolom:
                kolom.verwijder(te_verwijderen_kaart)
    
    #verwijdert een kaart uit de freecell
    def verwijder_uit_freecel(self, te_verwijderen_kaart):
        teller = 0
        for freecel in self.freecells:
            if te_verwijderen_kaart.nummer == freecel.nummer and te_verwijderen_kaart.soort == freecel.soort:
                self.freecells[teller] = Kaart(0, 'L')
            else:
                teller += 1
    
    #geeft het aantal weggespeelde kaarten terug
    def geef_aantal_weggespeelde_kaarten(self):
        aantal_weggespeelde_kaarten = 0
        for doelcel in self.doelcellen:
            aantal_weggespeelde_kaarten += doelcel.aantal 
        return aantal_weggespeelde_kaarten - 4 #-4 omdat er nog 4x een kaart met de waarde 0 'L' inzit
    
    #verplaatst een kaart naar een kolom waar hij zelf voorheen niet inzat
    def verplaats_naar_een_kolom(self, kaart): # deze moet nogmaals gechecked worden
        kolom_en_kaart = self.vind_kolom_en_kaart(kaart)
        if kaart.is_freecell(self):
            for kolom in self.kolommen:
                if kolom.aantal > 0:
                    if kaart.nummer == kolom.kaarten[-1].nummer - 1 and kaart.geef_kleur() != kolom.kaarten[-1].geef_kleur():
                        kolom.voeg_toe(kaart)
                        break
        else:
            for kolom in self.kolommen:
                if kolom != kolom_en_kaart[0]:
                    if kolom.aantal > 0:
                        if kaart.nummer == kolom.kaarten[-1].nummer - 1 and kaart.geef_kleur() != kolom.kaarten[-1].geef_kleur():
                            kolom.voeg_toe(kaart)
                            break
    
    #voegt een kaart toe aan een doelcel die beschikbaar 
    def voeg_toe_aan_doelcel(self, kaart):
        kolom_en_kaart = self.vind_kolom_en_kaart(kaart)
        for doelcel in self.doelcellen:
            if kaart.nummer == doelcel.kaarten[-1].nummer + 1 and kaart.soort == doelcel.kaarten[-1].soort:
                doelcel.voeg_toe(kaart)
                break
            elif doelcel.kaarten[-1].nummer == 0 and doelcel.kaarten[-1].soort == 'L':      
                doelcel.voeg_toe(kaart)
                break
    
    #voegt een kaart toe aan een freecell
    def voeg_toe_aan_freecel(self, kaart):
        teller = 0
        for freecell in self.freecells:
            if freecell.nummer == 0 and freecell.soort == 'L':
                self.freecells[teller] = kaart
                return True
            else:
                teller += 1
        
        #als de kaart niet aan een freecell toegevoegd kan worden, controleert de onderstaande loop of er een lege kolom is waar deze kaart in kan
        for kolom in self.kolommen:
            if kolom.aantal == 0:
                kolom.voeg_toe(kaart)
                return True
    
    #drukt het hele bord af in de console
    def druk_af(self):
        print 60*'-'
        print '{:^30}'.format('Freecells'),'|' '{:^30}'.format('Doelcellen')
        print 60*'-'
        for freecell in self.freecells:
            print '[{:2}{:1}] '.format(freecell.nummer, freecell.soort),
        print '{:^7}'.format('|'),
        for kolom in self.doelcellen:
            print '[{:2}{:1}] '.format(kolom.kaarten[-1].nummer, kolom.kaarten[-1].soort),
        print '\n' + 60*'-'
        mapped_kolommen = map(None, self.kolommen[0].kaarten, self.kolommen[1].kaarten, self.kolommen[2].kaarten,self.kolommen[3].kaarten,self.kolommen[4].kaarten,self.kolommen[5].kaarten, self.kolommen[6].kaarten, self.kolommen[7].kaarten)
        for kolom in mapped_kolommen:
            for kaart in kolom:
                if kaart == None:
                    print ' [   ] ',
                else:
                    print ' [{:2}{:1}] '.format(kaart.nummer, kaart.soort),
            print '\n'
        print 60*'-'

