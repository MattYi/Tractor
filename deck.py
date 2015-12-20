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
        currently the game is only played with 2 set of card
        which means number of cards is 108
        cards are stored as a list, the next one to be given out is at the end of the list
        ################################################################################
        #class members
        ################################################################################
        private
        self.cards 
            type list
        public:
        self.bottom
            type list
        self.top
            type list
        """
        num = np.hstack((np.arange(0,54),np.arange(0,54)))#a 1 by 108 matrix
        np.random.shuffle(num)
        self.cards = [] #private
        for item in num:
            self.cards.append(Card(item)) 

        self.__bottom = self.cards[0:8] #first 8 elements in the list are 8 "bottom cards" kept in deck 
        self.top = self.cards[8:] #self.cards only has 100 cards which will be drawn
    
    def shuffle(self):
        """
        To shuffle the deck, namely to randomly rearrange self.card
        No return value
        """
        #TODO: don't really need this function? It's essentially the same as __init__()
        num = np.hstack((np.arange(0,54),np.arange(0,54)))#a 1 by 108 matrix
        np.random.shuffle(num)
        self.cards = []
        for item in num:
            self.cards.append(Card(item)) 
        self.bottom = self.cards[0:8] #first 8 elements in the list are 8 "bottom cards" kept in deck 
        self.cards = self.cards[8:] #self.cards only has 100 cards which will be drawn
    
    #tested
    def popCard(self):
        """
        To give out a card
        Returned variable is a card object
        Length of self.card decrease by one each time after this func is called
        """
        return self.top.pop()

    #tested
    def changeBottom(self, get, put, debug = 0):
        """
        change 8 "bottom cards"
        -get is a list of cards requested from the "bottom cards"
        -put is a list of cards put back to the "bottom cards"
        -length of get must be equal to length of put
        -will return False if fail. Otherwise it will return True
        """
        if debug > 0:
            print "Bottom cards before changing:"
            self.displayBottom()
        if len(get) != len(put):
            print "Error! Number of Cards get from \"bottom cards\" is not the same as those of cards put back"
            return False
        elif len(get) > 8 or len(get) < 0:
            print "Error! Number of Cards requested from \"bottom cards\" is not in the range of 0 to 8"
            return False
        else:#delete all items of get in self.bottom and append put to it
            for item in get:
                if item not in self.bottom:
                    print "Try to get a card, ", item, " which is not in the \"bottom cards\"." 
                    return False
                else:
                    self.bottom.remove(item)
            self.bottom = self.bottom + put
            if debug > 0:
                print "Cards get from the bottom:"
                for item in get:
                    print item
                print "Cards put into the bottom:"
                for item in put:
                    print item
                print "Bottom cards after changing:"
                self.displayBottom()
            return True

    #tested
    def displayBottom(self):
        """
        Display cards in bottom cards.
        """
        print "Cards in the bottom:"
        for item in self.bottom:
            print item
        #print self.bottom[0]
        #print type(self.bottom)
        #return 0

    #tested
    def displayTop(self):
        """
        Display cards in top cards.
        """
        print "Cards in the top:"
        for item in self.top:
            print item
        
    #tested
    def displayCards(self):
        """
        Display all cards.
        """
        print "All cards:"
        for item in self.cards:
            print item

    #tested
    def getBottom(self):
        return self.__bottom

    #tested
    def getTop(self):
        return self.top

    #tested
    def nRemaining(self):
        return len(self.top)

                    



    
    
