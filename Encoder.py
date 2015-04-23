import sys
from utils import *
import CombGenerator as cg



baseVals = {'2':43,'3':89,'4':113,'5':173,'6':211,'7':293,'8':353,'9':389,'T':421,'J':457,'Q':503,'K':599,'A':701}






# def comparehands(hand1,hand2):
# 	if 



def enc(hand,comb):
	if comb == h.HIGH_CARD:
		return encHighCard(hand)




def encHighCard(hand):
	sm = 0
	for c in hand:
		sm += baseVals[c[0]] * baseVals[c[0]]
	return sm


def testCompareHighs(lp):
	for x in range(lp):
	    hCh = cg.generateAHandOfType(h.HIGH_CARD)
	    hCh2 = cg.generateAHandOfType(h.HIGH_CARD)
	    # print reduceHandRank(longSort(hCh)) , " VS ", reduceHandRank(longSort(hCh2))
	    # print getHighCardHandName(hCh), " VS ", getHighCardHandName(hCh2)
	    # print enc(hCh,h.HIGH_CARD) ,"  VS " , enc(hCh2,h.HIGH_CARD)
	    winner = hCh if enc(hCh,h.HIGH_CARD) > enc(hCh2,h.HIGH_CARD) else hCh2
	    looser = hCh if enc(hCh,h.HIGH_CARD) < enc(hCh2,h.HIGH_CARD) else hCh2
	    print getHighCardHandName(winner) ," BEATS " ,getHighCardHandName(looser)


testCompareHighs(10)


