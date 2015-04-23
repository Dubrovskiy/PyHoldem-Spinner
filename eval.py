import datetime
import time
from utils import *




def checkStraight(hand):
    red = reduceHandRank(hand)
    for straight in STRAIGHTS:
        str = []
        for card in red:
            if card in straight and card not in str: str+=card
            if len(str) == 5: return straight
    return None


def checkFlush(hand):
    suits = reduceHandSuit(hand)
    for x in range(0,4):
        if suits[x] != suits[x+1]: return None
    return hand



def checkStraightFlush(hand):
    if checkFlush(hand) and checkStraight(hand): return hand
    else: return None


def sort(hand):
    tmp = [0,0,0,0,0,0,0,0,0,0,0,0,0]
    for card in hand:
        tmp[getRankValue(card)] = card
    d = []
    for card in tmp:
        if (card!=0): d.append(card)
    return d


def getPairList(hand):
    tmp = [0,0,0,0,0,0,0,0,0,0,0,0,0]
    for card in hand:
        tmp[getRankValue(card)]+=1
    return tmp


def checkQuads(hand):
    tmp = getPairList(hand)
    for x in tmp:
        if x ==4 : return hand
    return None

def checkFullHouse(hand):
    tmp = getPairList(hand)
    for x in tmp:
        if x ==1 or x == 4: return None
    return hand


def checkTrips(hand):
    tmp = getPairList(hand)
    for x in tmp:
        if x ==3 and not checkFullHouse(hand): return hand
    return None

def checkTwoPair(hand):
    tmp = getPairList(hand)
    mark = 0
    for x in tmp:
        if x>2: return None
        if x ==1 : 
            mark+=1
            if mark > 1: return None
    return hand

def checkPair(hand):
    tmp = getPairList(hand)
    for x in tmp:
        if x>2: return None
        if x==2: return hand
    return None

 
#------------ 5 card Type evaluators----------------------

# 5-hand evaluator first attempt. 1 million hands in 121 seconds.
def evalHand1(hand):
    if checkStraightFlush(hand): return h.STRAIGHT_FLUSH
    elif checkQuads(hand): return h.QUADS
    elif checkFullHouse(hand): return h.FULL_HOUSE
    elif checkFlush(hand): return h.FLUSH
    elif checkStraight(hand): return h.STRAIGHT
    elif checkTrips(hand): return h.THREE_OF_A_KIND
    elif checkTwoPair(hand): return h.TWO_PAIR
    elif checkPair(hand): return h.PAIR
    else: return h.HIGH_CARD


# 5-hand evaluator first attempt. 1 million hands in 121 seconds.
# Million runs: 
# 102 seconds (9724 hands per second)
# 84 seconds (11833 hands per second)
# 87 seconds (11484 hands per second)
def evalHand2(hand):
    straight = checkStraight(hand)
    flush = None
    if straight:
        flush = checkFlush(hand)
        if flush:
            return h.STRAIGHT_FLUSH
        else: return h.STRAIGHT

    if flush: return h.FLUSH
    else: flush = flush = checkFlush(hand)
    if flush: return h.FLUSH
    
    pairList = getPairList(hand)
    p = None
    t = None
    for x in pairList:
        if (x!=0):
            if x == 4 :
                return h.QUADS
            elif x == 3 :
                t = True
                if p and t: return h.FULL_HOUSE
            elif x == 2 :
                if p: 
                    if t: return h.FULL_HOUSE
                    else : return h.TWO_PAIR
                p = True
                if p and t: return h.FULL_HOUSE


    if t: return h.THREE_OF_A_KIND
    elif p: return h.PAIR
    else: return h.HIGH_CARD





