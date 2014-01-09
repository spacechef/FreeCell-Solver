from Kolom import Kolom
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
        self.freecells = [None, None, None, None]
        self.doelcellen = [None, None, None, None]
    
    def maak_kolommen(self):
        for aantal_kolommen in range(self.aantal_kolommen):
            kolom = Kolom()
            self.rij_met_kolommen.append(kolom)

    def voeg_toe_aan_kolom(self, kaart, kolom):
        self.rij_met_kolommen[kolom].voeg_toe(kaart)
    
    def druk_af(self):
        print '{:^29}'.format('Freecells'), '{:^29}'.format('Doelcellen')
        print 58*'-'
        print '[{0[0]}] [{0[1]}] [{0[2]}] [{0[3]}]'.format(self.freecells) + ' X ' + '[{0[0]}] [{0[1]}] [{0[2]}] [{0[3]}]'.format(self.doelcellen)
        print 58*'-'
        mapped_kolommen = map(None, self.rij_met_kolommen[0].rij_met_kaarten, self.rij_met_kolommen[1].rij_met_kaarten, self.rij_met_kolommen[2].rij_met_kaarten,self.rij_met_kolommen[3].rij_met_kaarten,self.rij_met_kolommen[4].rij_met_kaarten,self.rij_met_kolommen[5].rij_met_kaarten, self.rij_met_kolommen[6].rij_met_kaarten, self.rij_met_kolommen[7].rij_met_kaarten)
        for kolom in mapped_kolommen:
            for kaart in kolom:
                if kaart == None:
                    print '[   ]',
                else: 
                    print '[{:2}{:1}]'.format(kaart.nummer, kaart.soort),
            print '\n'