from deck import Deck
from card import Card
import pdb

#test Deck.changeBottom()
#correct operation
d1 = Deck()
get = d1.getBottom()
get = get[0:3]
put = [Card(3),Card(5),Card(19)]
d1.changeBottom(get,put,debug = 1)

#try to put 4 cards into the bottom while require other than 4
put = [Card(3),Card(5),Card(19),Card(33)]
d1.changeBottom(get,put,debug = 1)

#try to require some cards that are not in the bottom
d2 = Deck()
get = d2.getBottom()
get = get[0:4]
get[0] = Card(1)#this is probably not in the bottom
put = [Card(3),Card(5),Card(19),Card(33)]
d1.changeBottom(get,put,debug = 1)




#test Deck.popCard()
d3 = Deck()
top1 = d3.getTop()
print "How many cards are in the top?"
print d3.nRemaining()
card1 = d3.popCard()
top1 = d3.getTop()
print "How many cards are in the top?"
print d3.nRemaining()
card2 = d3.popCard()
top1 = d3.getTop()
print "How many cards are in the top?"
print d3.nRemaining()
