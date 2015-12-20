from rule import *
import random
import card

r = Rule()
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
'''
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
'''

'''
test cardListContainTract:
'''
'''
cdList = []

for a in xrange(0,8):
    cd = card.Card(a)
    cdList.append(cd)
    cdList.append(cd)

for cd in cdList:
    print cd

print r.cardListContainTract(cdList, 6)
print r.cardListContainTract(cdList, 5)
print r.cardListContainTract(cdList, 4)
print r.cardListContainTract(cdList, 3)
print r.cardListContainTract(cdList, 2)
print r.cardListContainTract(cdList, 1)
print r.cardListContainTract(cdList, 0)
'''

'''
test isFollowingAllowed
test case 1: leading played a single trump, following did not play a trump while actually he has/doesnt have a trump in hand
test case 2: leading played a trump tract, following did not play a trump tract while actually he has a trump tract in hand
test case 3: same as 1, only not trump
test case 4: same as 2, only not trump
test case 5: leading played a combo of a single card and two tract:
test case 5.1: following dropped while still has card of the same suit
test case 5.2: following played 5 singleCard while still has a 1-len tract in hand
test case 5.3: following played 2 singleCard and a 1-len tract but still has 2-len tract in hand
test case 5.4: following played a 2-len tract while still has a 1-len tract in hand
'''

s2 = card.Card(0)
s3 = card.Card(1)
s4 = card.Card(2)
s6 = card.Card(4)
s7 = card.Card(5)
s8 = card.Card(6)
s9 = card.Card(7)
s10 = card.Card(8)
sJ = card.Card(9)
sQ = card.Card(10)
sK = card.Card(11)
sA = card.Card(12)
r2 = card.Card(13)
r3 = card.Card(14)
r4 = card.Card(15)
r5 = card.Card(16)
r6 = card.Card(17)
r7 = card.Card(18)
r9 = card.Card(19)
r10 = card.Card(20)
rJ = card.Card(21)
rQ = card.Card(22)
rK = card.Card(23)


'''
test isFollowingAllowed: leading is a single tract
'''

leadingCds = [s2, s3, s4, s6]
followingHand = [s7, s7, s8, s8, sJ, sJ, sQ, sK, sA, rK]
followingCds = [s7, s7, s8, rK]
print r.isFollowingAllowed(leadingCds, followingCds, followingHand)





