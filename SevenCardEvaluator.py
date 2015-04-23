from utils import *
import FiveCardEvaluator


# A 7 card evaluation (type) algorithm. 
# Million runs: 
# 93 seconds (10691 hands per second)
def eval(cards):
  
    z = getPairListZ(cards)
    zlength = len(z)
    f = checkFlush(cards)
    s = checkStraight(cards)

    if zlength >= 5:
       if checkStraightFlush(cards): return h.STRAIGHT_FLUSH
       elif f: return h.FLUSH
       elif s: return h.STRAIGHT
       elif zlength == 7: return h.HIGH_CARD
       elif zlength == 6: return h.PAIR

    if zlength == 5:
        if f and s: return h.STRAIGHT_FLUSH
        for i in z: 
            if i==3: return h.THREE_OF_A_KIND
        for i in z: 
            if i==2: return h.TWO_PAIR

    elif zlength == 4:
        t = None
        p = 0
        for i in z:
            if i==4: return h.QUADS
            elif i==3: t = True
            elif i==2: p +=1
            elif i==2: p+=1
        if t and p!=0: return h.FULL_HOUSE
        else: return h.TWO_PAIR

    elif zlength == 3:
        t = 0
        p = 0
        for i in z: 
            if i==4: return h.QUADS
            elif i==3: t+=1 
            elif i==2: p+=1
        if t>0 and p>0: return h.FULL_HOUSE
        elif t>1 : return h.FULL_HOUSE
        else: return h.FULL_HOUSE
    else: return h.QUADS

# Check straigh flush on more than 5 cards (special case)
def checkStraightFlush(hand):
    st = getDominantSuit(hand)
    if st[1]<5: return False

   
    std = [] 
    for c in hand:
        if (c[1]==st[0]):
            std.append(c)

    if len(std) < 5: return False
    return checkStraight(std)


# Checks if a straight is present. And if it is - returns the one.
def checkStraight(hand):
    red = reduceHandRank(hand)
    for straight in STRAIGHTS:
        str = []
        for card in red:
            if card in straight and card not in str: str+=card
            if len(str) == 5: return straight
    return None

# Checks if a straight is present. If it is returns the dominant suit tuple
def checkFlush(hand):
    stm = [0,0,0,0]
    suits = reduceHandSuit(hand)
    for x in range(0,7):
        if suits[x] == 's': stm[0]+=1
        elif suits[x] == 'c': stm[1]+=1
        elif suits[x] =='h': stm[2]+=1
        elif suits[x] == 'd': stm[3]+=1
    for s in stm:
        if (s >= 5 ): return getDominantSuit(hand)
    return None





def testEvaluatorDetailed():
    deck = generateDeck()
    cards = getSevenCardHand(deck)
    # cards = ['5c', 'Jc', '8s', '6c', '4c', '7c', '8d']
    print "Cards : ", cards
    print "RedR : ", reduceHandRank(longSort(cards))  
    print "RedS : ", str(sorted(reduceHandSuit(cards)))
    print "Zlist : ", getPairListZ(cards)
    print "Zlength : ", len(getPairListZ(cards))
    print  "Evaluation : ", eval(cards).name
    print "Evaluatuin from 5eval : ", FiveCardEvaluator.getBestOfSeven(cards)



# Testes the 7 card evaluator versus the 
def test7EvalVs5Eval(times):
    for x in range(0,times):
        deck = generateDeck()
        cards = getSevenCardHand(deck)
        eval7 = eval(cards)
        eval5 = FiveCardEvaluator.getBestOfSeven(cards)
        if (eval7!=eval5):
            print cards
            print eval7
            print eval5
    print "Outputs match!"




# An implementation based main on the use of iterator
def iterSevenEval():
    hand = ['5c', 'Jc', '8s', '6c', '4c', '7c', '8d']
    print hand




iterSevenEval()

