'''
Created on 8 Jan 2014

@author: spacechef
'''

class Kolom(object):

    def __init__(self):
        self.kaarten = []
        self.aantal = 0

    def voeg_toe(self, kaart):
        self.kaarten.append(kaart)
        self.aantal += 1

    def verwijder_kaart(self, kaart):
        self.kaarten.remove(kaart)
#
#     def druk_af(self):
#         teller = 0
#         for i in self.rij_met_kaarten:
#             print '[{0[teller]}]'.format(i)
#