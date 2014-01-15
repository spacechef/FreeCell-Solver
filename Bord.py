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

    def maak_doel_en_freecellen(self):
        for aantal_freecells in range(self.aantal_freecells):
            self.freecells.append(Kaart(0, 'L'))

        for aantal_doelcellen in range(self.aantal_doelcellen):
            doelcel = Kolom()
            self.doelcellen.append(doelcel)
            doelcel.voeg_toe(Kaart(0,'L'))

    def maak_kolommen(self):
        for aantal_kolommen in range(self.aantal_kolommen):
            kolom = Kolom()
            self.kolommen.append(kolom)
    
    def deel_kaarten(self, kaartspel):
        teller = 0
        for kaart in kaartspel.kaartspel:
            if teller == 8:
                teller = 0
            self.kolommen[teller].voeg_toe(kaart)
            teller += 1
    
    def geef_aantal_freecells(self):
        aantal_freecells = 0
        for kaart in self.freecells:
            if kaart.nummer == 0:
                aantal_freecells += 1

        return aantal_freecells
    
    def druk_af(self):
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

