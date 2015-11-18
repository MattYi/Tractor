'''
@author: MattYi, University of Washington
@date: 11/17/2015
'''

from card import *

class Deck(object):
    def __init__(self):
        # currently the game is only played by 2 set of card
        # which means the number of card is 108
        # the card are stored as a list, the next one to be given out is at the end of the list
        self.cards = range(0,108)   
    
    # to shuffle the deck  
    # which means to randomly rearrange the list self.card
    def shuffle(self):
        pass
    
    # to give out a card
    def popCard(self):
        pass
    
    