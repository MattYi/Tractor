'''
@author: MattYi, University of Washington
@date: 11/17/2015
'''

from card import Card
import numpy as np
import sys

class Deck(object):
    def __init__(self):
        """
        currently the game is only played by 2 set of card
        which means the number of card is 108
        cards are stored as a list, the next one to be given out is at the end of the list
        ################################################################################
        #class members
        ################################################################################
        self.cards() 
            type list
        self.under()
            type list
        """
        num = np.hstack((np.arange(0,54),np.arange(0,54)))#a 1 by 108 matrix
        np.random.shuffle(num)
        self.cards = []
        for item in num:
            self.cards.append(Card(item)) 
        self.under = self.cards[0:8] #first 8 elements in the list are 8 "bottom cards" kept in deck 
    
    def shuffle(self):
        """
        To shuffle the deck, namely to randomly rearrange self.card
        No return value
        """
        #TODO: don't really need this function? It's essentially the same as __init__()
        num = np.hstack((np.arange(0,53),np.arange(0,53)))#a 1 by 108 matrix
        np.random.shuffle(num)
        self.cards = []
        for i in len(num):
            self.cards.append(Card(num[i]))
    
    def popCard(self):
        """
        To give out a card
        Returned variable is a card object
        Length of self.card decrease by one each time after this func is called
        """
        return self.cards.pop()

    def changeBottom(self, get, put):
        """
        change 8 "bottom cards"
        -get is a list of cards somebody want from the "bottom cards"
        -put is a list of cards somebody put back to "bottom cards"
        -length of get must be equal to length of put
        """
        if len(get) != len(put):
            print "Error! Number of Cards get from \"bottom cards\" is not the same as those of cards put back"
            sys.exit()
        else:
            i = 0
            for item in get:
                if item in self.cards:
                    self.cards( self.cards.index(item) ) = put(i)
                    i = i+1
                else:
                    print "Error! Tried to get a card that is not in \"bottom cards\"!"
                    



    
    
