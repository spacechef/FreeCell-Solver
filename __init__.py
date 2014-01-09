from Kaart import Kaart
from Bord import Bord

'''
FreeCell Solver
Gemaakt op 08/01/2014
@author Spacechef
'''
bord = Bord()
bord.maak_kolommen()

def deel_kaarten():
    kaarten = range(52)
    teller = 0
    for i in kaarten:
        if teller == 8:
            teller = 0
        bord.rij_met_kolommen[teller].voeg_toe(i)
        teller += 1
        
# def print_kolommen():
#     for kolom in bord.rij_met_kolommen:
#         for kaart in kolom.rij_met_kaarten:            
#             print kaart,
#         print 'aantal: %d'  %kolom.aantal

deel_kaarten()
bord.druk_af()