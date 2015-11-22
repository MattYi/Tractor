import card
import cardSet
import random
import rule

'''
test singleCard
'''

'''
for i in xrange(30):
    a = random.randint(0,53)
    cd1 = card.card(a)
    sc1 = cardSet.singleCard(cd1)
    print str(a) + ' ' + str(cd1) + ' ' + str(sc1)
'''

'''
test Tract
'''

'''
for i in xrange(30):
    a = random.randint(0,53)
    b = random.randint(0,3)
    cd1 = card.card(a)
    t1 = cardSet.tract(cd1, b)
    print str([a,b]) + ' ' + str(t1)
'''

'''
test cardSet: __str__()
'''
'''
for i in xrange(30):
    a = random.randint(0,53)
    b = random.randint(0,3)
    cd1 = card.card(a)
    cd2 = card.card(a)
    t1 = cardSet.tract(cd1, b)
    print str([a,b]) + ' ' + str(cardSet.cardSet([cd1, cd2],[t1]))
'''

'''
test cardSet: isSingleCard, isTract, isCombol
'''
'''
for i in xrange(300):
    numSC = random.randint(0,5)
    scList = []
    for i in xrange(numSC):
        cd = card.card(random.randint(0,53))
        scList.append(cardSet.singleCard(cd))
    
    numT = random.randint(0,3)
    tList = []
    for i in xrange(numT):
        cd = card.card(random.randint(0,53))
        l = random.randint(1,3)
        t = cardSet.tract(cd,l)
        tList.append(t)
    cs = cardSet.cardSet(scList, tList)
    if cs.isCombol():
        print str(cs) + ' ' + 'isCombol'
    #if cs.isSingleCard():
        #print str(cs) + ' ' + 'isSingleCard'
    #if cs.isTract():
        #print str(cs) + ' ' + 'isTract'
'''


