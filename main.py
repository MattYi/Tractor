'''
from card import *

c1 = Card(105)
print c1
'''
from card import *
import random

tRank = '5'
tSuit = 'Diamond'

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
for i in xrange(20000):
    a = random.randint(0,53)
    b = random.randint(0,53)
    cardA = Card(a)
    cardB = Card(b)
    tmp = cardA.isNext(cardB, tRank, tSuit)
    if tmp == 1:
        print str(cardA) + " " + str(cardB) + " " + str(tmp)
'''

   


