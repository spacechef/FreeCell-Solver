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
seed = int(raw_input('Voer het gewenste spel in (tussen de 1 en de 11982): '))
kaartspel.maak(seed)
bord.maak_doel_en_freecellen()
bord.deel_kaarten(kaartspel)
bord.druk_af()

#geeft de beschikbare kaarten terug (kaarten waar de speler toegang tot heeft dit hoeft niet een speelbare kaart te zijn)
def geef_beschikbare_kaarten(diepte):
    beschikbare_kaarten = []
    for kolom in bord.kolommen:
        for level in range(diepte):
            if level < kolom.aantal:
                beschikbare_kaarten.append(kolom.kaarten[-1 - level])
    beschikbare_kaarten.extend(bord.freecells)
    return beschikbare_kaarten

#evalueert alle beschikbare kaarten en geeft deze een heuristische waarde. Geeft vervolgens alle geevalueerde kaarten terug
def evalueer_kaarten():
    beschikbare_kaarten = beschikbare_kaarten = geef_beschikbare_kaarten(1 + bord.geef_aantal_freecells())
    geevalueerde_kaarten = []
    for kaart in beschikbare_kaarten:
        heuristische_waarde = 0
        if kaart.is_freecell(bord) and kaart.kan_naar_een_doelcel(bord.doelcellen):
            heuristische_waarde = 100
        elif kaart.is_freecell(bord) and kaart.kan_naar_een_kolom(bord):
            heuristische_waarde = 70
        elif kaart.kan_naar_een_doelcel(bord.doelcellen):
            kolom_en_kaart = bord.vind_kolom_en_kaart(kaart)
            heuristische_waarde = 50 - kaart.diepte(bord) - kolom_en_kaart[0].geef_kolom_waarde()
        elif kaart.kan_naar_een_kolom(bord):
            kolom_en_kaart = bord.vind_kolom_en_kaart(kaart)
            heuristische_waarde = 20 - kaart.diepte(bord) - kolom_en_kaart[0].geef_kolom_waarde()

        geevalueerde_kaarten.append([kaart, heuristische_waarde])
    for kaart in geevalueerde_kaarten:
         print kaart[0].soort, kaart[0].nummer, 'waarde is:', kaart[1]
    return geevalueerde_kaarten

#bepaalt de beste kaart uit de lijst van geevalueerde kaarten en geeft deze terug
def beste_kaart(geevalueerde_kaarten):
    beste_kaart = None
    waarde = -50
    for geevalueerde_kaart in geevalueerde_kaarten:
        if geevalueerde_kaart[1] > waarde:
            beste_kaart = geevalueerde_kaart[0]
            waarde = geevalueerde_kaart[1]
    print 'Beste kaart is:', beste_kaart.nummer, beste_kaart.soort
    return beste_kaart

#kijkt welke zet er gedaan kan worden met de beste_kaart en doet deze zet. Zet vervolgens alle kolommen goed en verwijdert kaarten indien nodig
def speel_kaart(beste_kaart):
    if beste_kaart.kan_naar_een_doelcel(bord.doelcellen) and beste_kaart.is_direct_speelbaar(bord):
        bord.voeg_toe_aan_doelcel(beste_kaart)
        kolom_en_kaart = bord.vind_kolom_en_kaart(beste_kaart)
        bord.verwijder(beste_kaart, kolom_en_kaart[0])
        bord.druk_af()
    elif beste_kaart.kan_naar_een_kolom(bord) and beste_kaart.is_direct_speelbaar(bord):
        kolom_en_kaart = bord.vind_kolom_en_kaart(beste_kaart)
        bord.verplaats_naar_een_kolom(beste_kaart)
        bord.verwijder(beste_kaart, kolom_en_kaart[0])
        bord.druk_af()
    elif beste_kaart.kan_naar_een_doelcel(bord.doelcellen) and beste_kaart.is_freecell(bord):
        bord.voeg_toe_aan_doelcel(beste_kaart)
        bord.verwijder_uit_freecel(beste_kaart)
        bord.druk_af()
    elif beste_kaart.kan_naar_een_kolom(bord) and beste_kaart.is_freecell(bord):
        bord.verplaats_naar_een_kolom(beste_kaart)
        bord.verwijder_uit_freecel(beste_kaart)
        bord.druk_af()  
    elif beste_kaart.kan_naar_een_doelcel(bord.doelcellen):
        aantal_bovenliggende_kaarten = beste_kaart.diepte(bord)
        kolom_en_kaart = bord.vind_kolom_en_kaart(beste_kaart)
        te_verwijderen_kaarten = []
        for kaart in kolom_en_kaart[0].kaarten:
            if kolom_en_kaart[0].kaarten.index(kaart) >= kolom_en_kaart[0].aantal - aantal_bovenliggende_kaarten:
                bord.voeg_toe_aan_freecel(kaart)
                te_verwijderen_kaarten.append(kaart)
        for te_verwijderen_kaart in te_verwijderen_kaarten:
            kolom_en_kaart[0].verwijder(te_verwijderen_kaart)
        bord.voeg_toe_aan_doelcel(beste_kaart)
        bord.verwijder(beste_kaart, kolom_en_kaart[0])
        bord.druk_af()   
    elif beste_kaart.kan_naar_een_kolom(bord):
        aantal_bovenliggende_kaarten = beste_kaart.diepte(bord)
        kolom_en_kaart = bord.vind_kolom_en_kaart(beste_kaart)
        te_verwijderen_kaarten = []
        for kaart in kolom_en_kaart[0].kaarten:
            if kolom_en_kaart[0].kaarten.index(kaart) >= kolom_en_kaart[0].aantal - aantal_bovenliggende_kaarten:
                bord.voeg_toe_aan_freecel(kaart)
                te_verwijderen_kaarten.append(kaart) 
        bord.verplaats_naar_een_kolom(beste_kaart)
        for te_verwijderen_kaart in te_verwijderen_kaarten:
            kolom_en_kaart[0].verwijder(te_verwijderen_kaart)
        bord.verwijder(beste_kaart, kolom_en_kaart[0])
        bord.druk_af()

#houd laatst_gespeelde kaart bij zodat dezelfde kaart niet 2maal gespeeld gaat worden
laatst_gespeelde_kaart = None           
zet_mogelijk = True

#runned onderstaande functies zolang er een zet mogelijk is
while zet_mogelijk is True:
    geevalueerde_kaarten = evalueer_kaarten()
    de_beste_kaart = beste_kaart(geevalueerde_kaarten)
    if beste_kaart is None or laatst_gespeelde_kaart == de_beste_kaart:
        zet_mogelijk = False
        print 'Spel afgelopen! Aantal weggespeelde kaarten:', bord.geef_aantal_weggespeelde_kaarten()
        break
    speel_kaart(de_beste_kaart)
    laatst_gespeelde_kaart = de_beste_kaart