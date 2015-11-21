'''
from card import *

c1 = Card(105)
print c1
'''
from card import *
import random

tRank = 'A'
tSuit = 'None'

'''
Test class Card
'''

'''
Test Card.compare
Test case:

random tSuit, random tRank
random tSuit, tRank = A, 2
tSuit = None, random tRank
'''

'''
for i in xrange(30):
    a = random.randint(39,53)
    b = random.randint(39,53)
    cardA = Card(a)
    cardB = Card(b)
    tmp = cardA.compare(cardB, tRank, tSuit)
    print str(cardA) + " " + str(cardB) + " " + str(tmp)
'''

'''
Test Card.isNext
'''

'''
print Card(50).isNext(Card(25), tRank, tSuit)
print Card(12).isNext(Card(51), tRank, tSuit)
print Card(51).isNext(Card(52), tRank, tSuit)
print Card(52).isNext(Card(53), tRank, tSuit)
'''