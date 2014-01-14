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
            freecell = Kolom()
            self.freecells.append(freecell)
            freecell.voeg_toe(Kaart(0, 'L'))

        for aantal_doelcellen in range(self.aantal_doelcellen):
            doelcel = Kolom()
            self.doelcellen.append(doelcel)
            kaart = Kaart(0, 'L')
            doelcel.voeg_toe(kaart)

    def maak_kolommen(self):
        for aantal_kolommen in range(self.aantal_kolommen):
            kolom = Kolom()
            self.kolommen.append(kolom)

    def kaart_kan_naar_doelcel(self, kaart):
        for doelcel in self.doelcellen:
            if kaart.nummer == doelcel.kaarten[-1].nummer + 1 and kaart.soort == doelcel.kaarten[-1].soort:
                return True
            elif kaart.nummer == doelcel.kaarten[-1].nummer + 1 and doelcel.kaarten[-1].soort == 'L':
                return True

    def kaart_kan_naar_freecel(self, kaart):
        for freecel in self.freecells:
            if kaart.nummer == freecel.kaarten[-1].nummer + 1 and kaart.soort == freecel.kaarten[-1].soort:
                return True
            elif kaart.nummer == freecel.kaarten[-1].nummer + 1 and freecel.kaarten[-1].soort == 'L':
                return True

    def voeg_toe_aan_doelcel(self, kaart):
        teller = 0
        for doelcel in self.doelcellen:
            if doelcel.kaarten[-1].nummer == 0 or kaart.nummer == doelcel.kaarten[-1].nummer + 1 and kaart.soort == doelcel.kaarten[-1].soort: #hier moet soortcheck bij
                doelcel.voeg_toe(kaart)
                break
            else:
                teller +=1

    def voeg_toe_aan_freecel(self, kaart):
        teller = 0
        for freecell in self.freecells:
            if freecell.kaarten[-1].nummer == 0 or kaart.nummer == freecell.kaarten[-1].nummer + 1 and kaart.soort == freecell.kaarten[-1].soort: #hier moet soortcheck bij
                freecell.voeg_toe(kaart)
                break
            else:
                teller += 1

    def druk_af(self):
        print '{:^30}'.format('Freecells'),'|' '{:^30}'.format('Doelcellen')
        print 60*'-'
        for kolom in self.freecells:
            print '[{:2}{:1}] '.format(kolom.kaarten[-1].nummer, kolom.kaarten[-1].soort),
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

