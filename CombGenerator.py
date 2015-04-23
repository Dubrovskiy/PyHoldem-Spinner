from utils import *
import FiveCardEvaluator as eval5





def generateAHandOfType(handType):
    hand = None  
    while not hand:
        cards = getSevenCardHand(generateDeck())
        if eval5.evalHand2(cards)==handType: hand = cards
    return hand
    
	





def calcPossibleStartingHands():
    startingHands = []
    count = 0;
    for c1 in generateDeck():
        for c2 in generateDeck():
            hand = (c1,c2)
            if (c1!=c2 and hand not in startingHands): startingHands.append((c1,c2))
    return startingHands


def searchStartingHansdByCardRank(rank,rank2=None):
    if not rank2 : rank2 = rank
    l = []
    for hand in calcPossibleStartingHands():
        if (hand[0][0]==rank and hand[1][0]==rank2):
            l.append(hand)
    return l


def searchStartingHands(card,card2=None):
    l = []
    for hand in calcPossibleStartingHands():
        sch = True if not card2 else hand[1] == card2
        if (hand[0]==card and sch):
            l.append(hand)
    return l








