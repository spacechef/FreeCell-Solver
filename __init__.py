from Kaart import Kaart
from Bord import Bord
from KaartSpel import KaartSpel

'''
FreeCell Solver
Gemaakt op 08/01/2014
@author Spacechef
'''
bord = Bord()
kaartspel = KaartSpel()
bord.maak_kolommen()
kaartspel.maak()
# kaartspel.schud()


def deel_kaarten():
    teller = 0
    for kaart in kaartspel.kaartspel:
        if teller == 8:
            teller = 0
        bord.rij_met_kolommen[teller].voeg_toe(kaart)
        teller += 1
        
# def print_kolommen():
#     for kolom in bord.rij_met_kolommen:
#         for kaart in kolom.rij_met_kaarten:            
#             print kaart,
#         print 'aantal: %d'  %kolom.aantal

deel_kaarten()
bord.druk_af()