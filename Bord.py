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
        self.rij_met_kolommen = []
        self.aantal_freecells = 4
        self.freecells = []
        self.aantal_doelcellen = 4
        self.doelcellen = []
    
    def maak_doel_en_freecellen(self):
        for aantal_freecells in range(self.aantal_freecells):
            freecell = Kaart(0,'L')
            self.freecells.append(freecell)
        
        for aantal_doelcellen in range(self.aantal_doelcellen):
            doelcel = Kaart(0, 'L')
            self.doelcellen.append(doelcel)
            
    def maak_kolommen(self):
        for aantal_kolommen in range(self.aantal_kolommen):
            kolom = Kolom()
            self.rij_met_kolommen.append(kolom)

    def voeg_toe_aan_kolom(self, kaart, kolom):
        self.rij_met_kolommen[kolom].voeg_toe(kaart)
    
    def kaart_kan_naar_doelcel(self, kaart):
        for doelcel in self.doelcellen:
            if kaart.nummer == doelcel.nummer + 1 and kaart.soort == doelcel.soort:
                return True
            elif kaart.nummer == doelcel.nummer + 1 and doelcel.soort == 'L':
                return True
    
    def kaart_kan_naar_freecel(self, kaart):
        for freecel in self.freecells:
            if kaart.nummer == freecel.nummer + 1 and kaart.soort == freecel.soort:
                return True
            elif kaart.nummer == freecel.nummer + 1 and freecel.soort == 'L':
                return True
    
    def voeg_toe_aan_doelcel(self, kaart):
        teller = 0
        for doelcel in self.doelcellen:
            if doelcel.nummer == 0 or kaart.nummer == doelcel.nummer + 1 and kaart.soort == doelcel.soort: #hier moet soortcheck bij
                self.doelcellen[teller] = kaart
                break
            else:
                teller +=1
    
    def voeg_toe_aan_freecel(self, kaart):
        teller = 0
        for freecell in self.freecells:
            if freecell.nummer == 0 or kaart.nummer == freecell.nummer + 1 and kaart.soort == freecell.soort: #hier moet soortcheck bij
                self.freecells[teller] = kaart
                break
            else:
                teller += 1
    
    def druk_af(self):
        print '{:^30}'.format('Freecells'),'|' '{:^30}'.format('Doelcellen')
        print 60*'-'
        for kaart in self.freecells:
            print '[{:2}{:1}] '.format(kaart.nummer, kaart.soort),
        print '{:^7}'.format('|'),
        for kaart in self.doelcellen:
            print '[{:2}{:1}] '.format(kaart.nummer, kaart.soort),
        print '\n' + 60*'-'
        mapped_kolommen = map(None, self.rij_met_kolommen[0].rij_met_kaarten, self.rij_met_kolommen[1].rij_met_kaarten, self.rij_met_kolommen[2].rij_met_kaarten,self.rij_met_kolommen[3].rij_met_kaarten,self.rij_met_kolommen[4].rij_met_kaarten,self.rij_met_kolommen[5].rij_met_kaarten, self.rij_met_kolommen[6].rij_met_kaarten, self.rij_met_kolommen[7].rij_met_kaarten)
        for kolom in mapped_kolommen:
            for kaart in kolom:
                if kaart == None:
                    print ' [   ] ',
                else: 
                    print ' [{:2}{:1}] '.format(kaart.nummer, kaart.soort),
            print '\n'
        print 60*'-'
    
    