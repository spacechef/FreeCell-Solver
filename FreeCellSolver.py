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
bord.deel_kaarten(kaartspel)
bord.druk_af()

def geef_beschikbare_kaarten(diepte):
    beschikbare_kaarten = []
    for kolom in bord.kolommen:
        print len(kolom.kaarten)
        for level in range(diepte):
            if level < len(kolom.kaarten):
                beschikbare_kaarten.append(kolom.kaarten[-1 - level]) #deze moet in per beurt opgehoogd worden
    beschikbare_kaarten.extend(bord.freecells)
    return beschikbare_kaarten

hallo = geef_beschikbare_kaarten(1 + bord.geef_aantal_freecells())



for kaart in hallo:
    waarde = 0
#     if kaart.kan_naar_een_doelcel(bord.doelcellen):
#         kaart.verplaats_naar_een_doelcel
#          waarde += 50
    if kaart.kan_naar_een_kolom(bord.kolommen):
        kaart.verplaats_naar_kolom(bord.kolommen)
#         waarde += 20
        bord.druk_af
    


# def speel_kaart():
#     aantal_freecells = bord.aantal_freecells
# 
#     # check alle direct speelbare kaarten (laatste index van kolommen + freecells)
#     # check voor elke van deze kaarten of een van de doelcellen - kaartnummer 1 is
#         # zo ja -> verwijder de kaarten die ervoor liggen (eerst kijken of je hem in een kolom kwijt kan, daarna naar freecell) en speel naar doelcel
#         # zo nee -> kijk of het aantal freecells (lege kolommen + freecells) groter is dan de teller
#             # zo ja -> kijk een niveau dieper
#             #de freecell checker klopt niet want hij kijkt niet of de kaart daadwerkelijk gespeeld kan worden dus blijft hij altijd tot 4 diepte kijken ipv of de kaat gespeeld kan worden
#     for kolom in bord.kolommen:
#         aantal_freecells = bord.aantal_freecells 
#         speelbare_kaarten = kolom.kaarten[-aantal_freecells:] #deze moet in per beurt opgehoogd worden
#         for kaart in speelbare_kaarten:
#             if bord.kaart_kan_naar_doelcel(kaart):
#                 bord.voeg_toe_aan_doelcel(kaart)
#                 zet_kaarten_goed(kaart, kolom)
#                 bord.druk_af()
#                 break
# #                 freecel_naar_doelcel() #probeersel
#             elif bord.kaart_kan_naar_freecel(kaart):
#                 bord.voeg_toe_aan_freecel(kaart)
#                 zet_kaarten_goed(kaart, kolom)
#                 bord.druk_af()
#                 break
# #                 freecel_naar_doelcel() #probeersel
# 
# def freecel_naar_doelcel(): #probeersel
#     for freecel in bord.freecells:
#         for kaart in freecel:
#             if bord.kaart_kan_naar_doelcel(kaart):
#                 bord.voeg_toe_aan_doelcel(kaart)
#                 zet_kaarten_goed(kaart, freecel)
#                 bord.druk_af()
# 
# 
# def zet_kaarten_goed(kaart, kolom):
#     index = kolom.kaarten.index(kaart)    
#     del kolom.kaarten[index]
#     bovenliggende_kaarten = kolom.kaarten[index:]
#     print bovenliggende_kaarten
#     for kaart in kolom.kaarten:
#         print kaart.nummer, kaart.soort
#     print index
# 
#     for kaart in bovenliggende_kaarten: #haalt de laatste kaart nog niet weg
#          bord.voeg_toe_aan_freecel(kaart)
#          kolom.verwijder_kaart(kaart)