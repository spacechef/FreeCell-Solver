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
kaartspel.schud()
bord.maak_doel_en_freecellen()

def deel_kaarten():
    teller = 0
    for kaart in kaartspel.kaartspel:
        if teller == 8:
            teller = 0
        bord.rij_met_kolommen[teller].voeg_toe(kaart)
        teller += 1

def doe_zet():
    bepaal_speelbare_kaarten()
#     verplaats_speelbare_kaart_naar_doelcel()
def bepaal_aantal_freecells():
    aantal_freecells = 0
    for kaart in bord.freecells:
        if kaart.nummer == 0:
            aantal_freecells +=1
            
    return aantal_freecells
def speel_kaart():
    aantal_freecells = bord.aantal_freecells
    
    for kolom in bord.rij_met_kolommen:
        speelbare_kaarten_in_kolom = kolom.rij_met_kaarten[-aantal_freecells:]
        for kaart in speelbare_kaarten_in_kolom:
            if bord.kaart_kan_naar_doelcel(kaart):
                bord.voeg_toe_aan_doelcel(kaart)
                zet_kaarten_goed(kaart, kolom)
                bord.druk_af()
            elif bord.kaart_kan_naar_freecel(kaart):
                bord.voeg_toe_aan_freecel(kaart)
                zet_kaarten_goed(kaart, kolom)
                bord.druk_af()
            
            
def bepaal_speelbare_kaarten():
    aantal_freecells = bepaal_aantal_freecells()
    
    for kolom in bord.rij_met_kolommen:
        speelbare_kaarten_in_kolom = kolom.rij_met_kaarten[-aantal_freecells:]
        for kaart in speelbare_kaarten_in_kolom:
            for doelcel in bord.doelcellen: #dit moet denk ik in 4 aparte if'jes ivm overbodig vaak checken nu
                if kaart.nummer == doelcel.nummer + 1 and kaart.soort == doelcel.soort: #hier moet nog kleurcheck bij en de freecell en doelcellen moeten kaartobjecten worden
                    
                    zet_kaarten_goed(kaart, kolom)
                    print kaart.nummer, kaart.soort
                    print kaart
                    bord.voeg_toe_aan_doelcel(kaart)
#                     kolom.verwijder_kaart(kaart)
                    bord.druk_af()
                    break
                elif kaart.nummer == doelcel.nummer + 1 and doelcel.soort == 'L':
                    zet_kaarten_goed(kaart, kolom)
                    bord.voeg_toe_aan_doelcel(kaart)
#                     print kaart.nummer, kaart.soort
                    print kaart
#                     kolom.verwijder_kaart(kaart)
                    bord.druk_af()                                  
#             if kaart.nummer == bord.doelcellen[0].nummer + 1 and kaart.soort == 
def zet_kaarten_goed(kaart, kolom):
    index = kolom.rij_met_kaarten.index(kaart)
    #aantal_bovenliggende_kaarten = len(kolom.rij_met_kaarten) - index
    del kolom.rij_met_kaarten[index]
    for kaart in kolom.rij_met_kaarten:
        print kaart.nummer, kaart.soort
    print index
    for kaart in kolom.rij_met_kaarten: #haalt de laatste kaart nog niet weg
        if kolom.rij_met_kaarten.index(kaart) >= index:
           kolom.verwijder_kaart(kaart)

#     for nummer, kaart in enumerate(kolom.rij_met_kaarten):
#         if nummer > index:
#             bord.voeg_toe_aan_freecel(kaart)
#             kolom.verwijder_kaart(kaart)
#     for aantal in range(1, aantal_bovenliggende_kaarten): #range is 1 tot aantal_bovenliggende kaarten anders speelt hij de gespeelde kaart nog een x (dubbel) naar de freecell
#         bord.voeg_toe_aan_freecel(kolom.rij_met_kaarten[index + aantal]) #lelijke code nog een x naar kijken + hier gaat wat fout met index cijfers
#         kolom.verwijder_kaart(kolom.rij_met_kaarten[index + aantal]) #hier ook iets fout
                       
            
# def print_kolommen():
#     for kolom in bord.rij_met_kolommen:
#         for kaart in kolom.rij_met_kaarten:            
#             print kaart,
#         print 'aantal: %d'  %kolom.aantal

deel_kaarten()
bord.druk_af()
speel_kaart()