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
        for level in range(diepte):
            if level < len(kolom.kaarten):
                beschikbare_kaarten.append(kolom.kaarten[-1 - level]) #deze moet in per beurt opgehoogd worden
    beschikbare_kaarten.extend(bord.freecells)
    return beschikbare_kaarten


levend = True
while levend == True:
    hallo = geef_beschikbare_kaarten(1 + bord.geef_aantal_freecells())
    for kaart in hallo:
        if kaart.is_direct_speelbaar(bord):
            if kaart.kan_naar_een_doelcel(bord.doelcellen):
                kaart.voeg_toe_aan_doelcel(bord)
                bord.druk_af()
            if kaart.kan_naar_een_kolom(bord.kolommen):
                kaart.verplaats_naar_een_kolom(bord)
                bord.druk_af()

#     # check alle direct speelbare kaarten (laatste index van kolommen + freecells)
#     # check voor elke van deze kaarten of een van de doelcellen - kaartnummer 1 is
#         # zo ja -> verwijder de kaarten die ervoor liggen (eerst kijken of je hem in een kolom kwijt kan, daarna naar freecell) en speel naar doelcel
#         # zo nee -> kijk of het aantal freecells (lege kolommen + freecells) groter is dan de teller
#             # zo ja -> kijk een niveau dieper
#             #de freecell checker klopt niet want hij kijkt niet of de kaart daadwerkelijk gespeeld kan worden dus blijft hij altijd tot 4 diepte kijken ipv of de kaat gespeeld kan worden