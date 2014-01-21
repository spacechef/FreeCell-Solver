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
# kaartspel.maak_oplosbaar_spel()
kaartspel.schud()
bord.maak_doel_en_freecellen()
bord.deel_kaarten(kaartspel)
bord.druk_af()

def geef_beschikbare_kaarten(diepte):
    beschikbare_kaarten = []
    for kolom in bord.kolommen:
        for level in range(diepte):
            if level < len(kolom.kaarten):
                beschikbare_kaarten.append(kolom.kaarten[-1 - level])
    beschikbare_kaarten.extend(bord.freecells)
    return beschikbare_kaarten

def evalueer_kaarten():
    beschikbare_kaarten = beschikbare_kaarten = geef_beschikbare_kaarten(1 + bord.geef_aantal_freecells())
    geevalueerde_kaarten = []
    for kaart in beschikbare_kaarten:
        heuristische_waarde = 0
        if kaart.is_freecell(bord) and kaart.kan_naar_een_doelcel(bord.doelcellen):
            heuristische_waarde = 100
        elif kaart.is_freecell(bord) and kaart.kan_naar_een_kolom(bord.kolommen):
            heuristische_waarde = 70
        elif kaart.kan_naar_een_doelcel(bord.doelcellen):
            heuristische_waarde = 50 - kaart.diepte(bord)   
        elif kaart.kan_naar_een_kolom(bord.kolommen):
            heuristische_waarde = 20 - kaart.diepte(bord)

        geevalueerde_kaarten.append([kaart, heuristische_waarde])
    for kaart in geevalueerde_kaarten:
         print kaart[0].soort, kaart[0].nummer, 'waarde is:', kaart[1]
    return geevalueerde_kaarten

def beste_kaart(geevalueerde_kaarten):
    beste_kaart = None
    waarde = -50
    for geevalueerde_kaart in geevalueerde_kaarten:
        if geevalueerde_kaart[1] > waarde:
            beste_kaart = geevalueerde_kaart[0]
            waarde = geevalueerde_kaart[1]
    print 'Beste kaart is:', beste_kaart.nummer, beste_kaart.soort
    return beste_kaart

def speel_kaart(beste_kaart):
    if beste_kaart.kan_naar_een_doelcel(bord.doelcellen) and beste_kaart.is_direct_speelbaar(bord):
        beste_kaart.voeg_toe_aan_doelcel(bord)
        kolom_en_kaart = bord.vind_kolom_en_kaart(beste_kaart)
        bord.verwijder(beste_kaart, kolom_en_kaart[0])
        bord.druk_af()
    elif beste_kaart.kan_naar_een_kolom(bord.kolommen) and beste_kaart.is_direct_speelbaar(bord):
        kolom_en_kaart = bord.vind_kolom_en_kaart(beste_kaart)
        beste_kaart.verplaats_naar_een_kolom(bord)
        bord.verwijder(beste_kaart, kolom_en_kaart[0])
        bord.druk_af()
    elif beste_kaart.kan_naar_een_doelcel(bord.doelcellen) and beste_kaart.is_freecell(bord):
        beste_kaart.voeg_toe_aan_doelcel(bord)
        bord.verwijder_uit_freecel(beste_kaart)
        bord.druk_af()
    elif beste_kaart.kan_naar_een_kolom(bord.kolommen) and beste_kaart.is_freecell(bord):
        beste_kaart.verplaats_naar_een_kolom(bord)
        bord.verwijder_uit_freecel(beste_kaart)
        bord.druk_af()  
    elif beste_kaart.kan_naar_een_doelcel(bord.doelcellen):
        aantal_bovenliggende_kaarten = beste_kaart.diepte(bord)
        kolom_en_kaart = bord.vind_kolom_en_kaart(beste_kaart)
        te_verwijderen_kaarten = []
        for kaart in kolom_en_kaart[0].kaarten:
            if kolom_en_kaart[0].kaarten.index(kaart) >= len(kolom_en_kaart[0].kaarten) - aantal_bovenliggende_kaarten:
                kaart.voeg_toe_aan_freecel(bord)
                te_verwijderen_kaarten.append(kaart)
        for te_verwijderen_kaart in te_verwijderen_kaarten:
            kolom_en_kaart[0].verwijder(te_verwijderen_kaart)
        beste_kaart.voeg_toe_aan_doelcel(bord)
        bord.verwijder(beste_kaart, kolom_en_kaart[0])
        bord.druk_af()   
    elif beste_kaart.kan_naar_een_kolom(bord.kolommen):
        aantal_bovenliggende_kaarten = beste_kaart.diepte(bord)
        kolom_en_kaart = bord.vind_kolom_en_kaart(beste_kaart)
        te_verwijderen_kaarten = []
        for kaart in kolom_en_kaart[0].kaarten:
            if kolom_en_kaart[0].kaarten.index(kaart) >= len(kolom_en_kaart[0].kaarten) - aantal_bovenliggende_kaarten:
                kaart.voeg_toe_aan_freecel(bord)
                te_verwijderen_kaarten.append(kaart) 
        beste_kaart.verplaats_naar_een_kolom(bord)
        for te_verwijderen_kaart in te_verwijderen_kaarten:
            kolom_en_kaart[0].verwijder(te_verwijderen_kaart)
        bord.verwijder(beste_kaart, kolom_en_kaart[0])
        bord.druk_af()
        
laatst_gespeelde_kaart = None           
zet_mogelijk = True
while zet_mogelijk is True:
    geevalueerde_kaarten = evalueer_kaarten()
    de_beste_kaart = beste_kaart(geevalueerde_kaarten)
    if beste_kaart is None or laatst_gespeelde_kaart == de_beste_kaart:
        zet_mogelijk = False
        print 'Spel afgelopen! Aantal weggespeelde kaarten:', bord.geef_aantal_weggespeelde_kaarten()
        break
    speel_kaart(de_beste_kaart)
    laatst_gespeelde_kaart = de_beste_kaart