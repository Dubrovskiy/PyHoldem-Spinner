from enum import Enum
import itertools
import random


SUITS = ['s','c','h','d']
SUIT_NAMES = ['spades','clubs','hearts','diamonds']



RANKS = ['2','3','4','5','6','7','8','9','T','J','Q','K','A']
RANK_NAMES = ['Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace']




# Combinations
class h(Enum):
    HIGH_CARD = 1
    PAIR = 2
    TWO_PAIR = 3
    THREE_OF_A_KIND= 4
    STRAIGHT = 5
    FLUSH = 6
    FULL_HOUSE = 7
    QUADS = 8
    STRAIGHT_FLUSH = 9




STRAIGHTS = [
"A2345",
"23456",
"34567",
"45678",
"56789",
"6789T",
"789TJ",
"89TJQ",
"9TJQK",
"TJQKA"
]


PAIRS = [ "AA","KK","QQ","JJ","TT","99","88","77","66","55","44","33","22"]
TRIPS = [ "AAA","KKK","QQQ","JJJ","TTT","999","888","777","666","555","444","333","222"]
QUADS = [ "AAAA","KKKK","QQQQ","JJJJ","TTTT","9999","8888","7777","6666","5555","4444","3333","2222"]



def getRankName(rank):
    return RANK_NAMES[RANKS.index(rank)]

def getSuitName(suit):
    return SUIT_NAMES[SUITS.index(suit)]		

def getCardName(card):
	return getRankName(card[0]) + " of " + getSuitName(card[1])

def getStraightName(straight):
	return getRankName(straight[4]) + " high straight"

def getRankValue(card):
	return RANKS.index(card[0])

def getHighCardHandName(hand):
    hand = longSort(hand)
    hc= hand[len(hand)-1]
    k = hand[len(hand)-2]

    str = "(%s HIGH + %s kicker)" %(getRankName(hc[0]),getRankName(k[0]))
    return str



# A method that generates and returns the 52 deck (already shuffled)
def generateDeck():
    deck = []
    for val in RANKS:
       for suit in SUITS:
          card = "%s%s" % (val,suit)
          deck.append(card)
    random.shuffle(deck)
    return deck


# Method that pops 5 cards from a given deck and returns it as a new array
def getHand(deck):
    hand = []
    for x in range(0,5):
        hand.append(deck.pop())
    return hand  

# Method that pops 7 cards from a given deck and returns it as a new array
def getSevenCardHand(deck):
    hand = []
    for x in range(0,7):
        hand.append(deck.pop())
    return hand 


def getDominantSuit(hand):
    d = {'s':0,'c':0,'h':0,'d':0}
    for c in hand:
        d[c[1]]+=1
    mx = 0
    m = None
    for k in d:
        if d[k]>mx: 
            mx = d[k]
            m = k

    return (m,mx)

def reduceHandRank(hand):
    vals = ""
    for card in hand:
        vals+=card[0]
    return vals

def reduceHandSuit(hand):
    suits = ""
    for card in hand:
        suits+=card[1]
    return suits


def getPairList(hand):
    tmp = [0,0,0,0,0,0,0,0,0,0,0,0,0]
    for card in hand:
        tmp[getRankValue(card)]+=1
    return tmp

def getPairListZ(hand):
    z = []
    tmp = getPairList(hand)
    for val in tmp:
        if val != 0: z.append(val)
    return z
    

def perm7(cards):
    return set(itertools.combinations(cards, 5))



def genFulls():
    deck = generateDeck()



# simple sorting (very slow), debugging purposes mainly
def longSort(hand):
  tmp = []
  for rank in RANKS:
      for card in hand:
          if card[0]==rank:
              tmp.append(card)
  return tmp



