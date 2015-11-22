from rule import *
import random
import card

r = rule()
r.setTrumpRank('5')
r.setTrumpSuit('Spade')

'''
test rule.getCardPnt(cd)
test passed
'''

'''
r = rule()
r.setTrumpRank('5')
r.setTrumpSuit('Heart')

for i in xrange(0,54):
    cd = card.Card(i)
    print str(cd) + ' ' + str(r.getCardPnt(cd))
'''

'''
r = rule()
r.setTrumpRank('A')
r.setTrumpSuit('Heart')

for i in xrange(0,54):
    cd = card.Card(i)
    print str(cd) + ' ' + str(r.getCardPnt(cd))
'''

'''
r = rule()
r.setTrumpRank('2')
r.setTrumpSuit('None')

for i in xrange(0,54):
    cd = card.Card(i)
    print str(cd) + ' ' + str(r.getCardPnt(cd))
'''

# test is drop

'''
for i in xrange(500000):
    cd1 = card.card(random.randint(0,53))
    cd2 = card.card(random.randint(0,53))
    cd3 = card.card(random.randint(0,53))
    if not r.isDrop([cd1,cd2,cd3]) and r.isTrump(cd1):
        print str(cd1) + ' ' + str(cd2) + ' ' + str(cd3) + ' ' + str(r.isDrop([cd1,cd2,cd3]))
'''
'''
cd1 = card.card(3)
cd2 = card.card(53)
print r.isTrump(cd1)
print r.isTrump(cd2)
print str(cd1) + ' ' + str(cd2) + ' ' + str(r.isDrop([cd1,cd2]))
'''

'''
test rearrange
'''

'''
for x in xrange(0,30):
    cdList = []
    for a in xrange(5):
        b = random.randint(0,53)
        cdList.append(card.card(b))
    print x
    for cd in cdList:
        print cd
    r.rearrange(cdList)
    print "rearrange"
    for cd in cdList:
        print cd, r.getCardPnt(cd)
'''

'''
test getCardSet()
'''

# test singlecard: passed

# test tract

for a in range(0, 8):
    b = a + 1
    cd1 = card.card(a)
    cd2 = card.card(b)
    cd3 = card.card(10)
    cdList = [cd1, cd1, cd2, cd3, cd2]
    for i in cdList:
        print i
    if r.isDrop(cdList):
        print 'isDrop'
    else:
        print r.getCardSet(cdList)
        


