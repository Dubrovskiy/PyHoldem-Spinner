import FiveCardEvaluator as fiveCardEval
import SevenCardEvaluator as sevenCardEval
from utils import *
import time





start = time.time()
handsToEvaluate = 10000
print "Started:"



for c in range(0,handsToEvaluate):
    hand = getSevenCardHand(generateDeck())
    e2 = fiveCardEval.getBestOfSeven(hand)



end = time.time()
elapsed = end - start
print "%d hands evaluated in %d seconds (%d hands per second)" % (handsToEvaluate,elapsed,(handsToEvaluate/elapsed))