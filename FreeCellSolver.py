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

def bepaal_aantal_freecells():
    aantal_freecells = 0
    for kaart in bord.freecells:
        if kaart.nummer == 0:
            aantal_freecells +=1

    return aantal_freecells

def speel_kaart():
    aantal_freecells = bord.aantal_freecells

    # check alle direct speelbare kaarten (laatste index van kolommen + freecells)
    # check voor elke van deze kaarten of een van de doelcellen - kaartnummer 1 is
        # zo ja -> verwijder de kaarten die ervoor liggen (eerst kijken of je hem in een kolom kwijt kan, daarna naar freecell) en speel naar doelcel
        # zo nee -> kijk of het aantal freecells (lege kolommen + freecells) groter is dan de teller
            # zo ja -> kijk een niveau dieper

    for kolom in bord.rij_met_kolommen: #de freecell checker klopt niet want hij kijkt niet of de kaart daadwerkelijk gespeeld kan worden dus blijft hij altijd tot 4 diepte kijken ipv of de kaat gespeeld kan worden
        speelbare_kaarten = kolom.kaarten[-aantal_freecells:] #deze moet in per beurt opgehoogd worden

        for kaart in speelbare_kaarten:
            if bord.kaart_kan_naar_doelcel(kaart):
                bord.voeg_toe_aan_doelcel(kaart)
                zet_kaarten_goed(kaart, kolom)
                bord.druk_af()
                freecel_naar_doelcel() #probeersel
            elif bord.kaart_kan_naar_freecel(kaart):
                bord.voeg_toe_aan_freecel(kaart)
                zet_kaarten_goed(kaart, kolom)
                bord.druk_af()
                freecel_naar_doelcel() #probeersel

def freecel_naar_doelcel(): #probeersel
    for freecel in bord.freecells:
        for kaart in freecel:
            if bord.kaart_kan_naar_doelcel(kaart):
                bord.voeg_toe_aan_doelcel(kaart)
                zet_kaarten_goed(kaart, freecel)
                bord.druk_af()


def zet_kaarten_goed(kaart, kolom):
    index = kolom.kaarten.index(kaart)
    for kaart in kolom.kaarten:
        print kaart.nummer, kaart.soort
    print index
#     del kolom.kaarten[index]
    for kaart in kolom.kaarten: #haalt de laatste kaart nog niet weg
        if kolom.kaarten.index(kaart) > index: #index positie van bovenliggende kaart veranderd doordat er een entry verwijderd word
            bord.voeg_toe_aan_freecel(kaart)
            kolom.verwijder_kaart(kaart)

deel_kaarten()
bord.druk_af()

levend = True
while levend == True:
    speel_kaart()