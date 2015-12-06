from player import Player
from deck import Deck
from card import Card
from brainTest import BrainTest


b1 = BrainTest()
p1 = Player(b1)
print "Info of p1:"
print p1
p1.setID(3)
p1.setName("Shawn")
print "Info of p1:"
print p1
d1 = Deck()
print "Check if Hands of p1 is empty:"
if p1.handIsEmpty():
    print "Yes!"
else:
    print "No!"
print "Hands of p1 at the beginning"
p1.displayHands()
cd1 = d1.popCard()
p1.drawCard(cd1)
cd1 = d1.popCard()
p1.drawCard(cd1)
cd1 = d1.popCard()
p1.drawCard(cd1)
cd1 = d1.popCard()
p1.drawCard(cd1)
print "Hands of p1 after drawing for 4 times"
p1.displayHands()
print "\n\n"

################################################################################
#test declareTrump()
cdOnDesk = [[],[],[]]
declareCards = p1.declareTrump(cdOnDesk)
if declareCards == False:#not declared
    print str(p1) + " does not want to declare trump."
else:#delcare trump
    print str(p1) + " want to declare trump using these cards:"
    for item in declareCards:
        print item
print "\n\n"

################################################################################
#test replaceBottom()
print "Old bottom:"
for item in d1.getBottom():
    print item
newBottom = p1.replaceBottom(d1.getBottom())
print "Try to replace the bottom with these cards:"
for item in newBottom:
    print item

print "deck.bottom should not have been changed at this stage since we need Game to call deck.changeBottom() to Actually change deck.bottom"
print "Let's check if deck.bottom is still the old one:"
for item in d1.getBottom():
    print item
print "\n\n"



################################################################################
#test declareToPlayCards()
cardToBePlayed1 = p1.declareToPlayCards(cdOnDesk)
print str(p1) + " tried to play: "
for item in cardToBePlayed1:
    print item

#check if cardToBePlayed1 obey the rules
#if it obey the rules:
p1.playCards(cardToBePlayed1)
#otherwise do nothing or perhaps call p1.declareToPlayCards() again

print "Hands of p1 after play some cards"
p1.displayHands()
print "\n\n"

