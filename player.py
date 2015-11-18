'''
@author: MattYi, University of Washington
@date: 11/17/2015
'''
from card import *

class Player(object):
    def __init__(self, pid = -1, n = "NoName"):
    # id: from 0 to 3, since currently we only consider the situation that there are 4 players
        self.id = pid
        self.name = n
    # hand: it is a list of card object that this player is holding
    # I don't know whether it is better to store the id or the object of card in the list
        self.hand = []
    
    def setName(self, n):
        self.name = n
        
    def getName(self, n):
        return self.name
    
    def setID(self,pid):
        self.id = pid
    
    def getID(self):
        return self.id
    
    def emptyHand(self):
        return self.hand.empty()
    
    # add the card to the self.hand
    def getCard(self, cd):
        pass
    
    # returns the unit of the trump
    # still confusing
    def setTrump(self, cd):
        pass
    
    # remove the card from the player
    # return the card
    # don't know yet the variable cd is the id of the card or the object
    # currently consider it as the object
    def playCards(self, cds):
        for cd in cds:
            if cd not in self.hand:
                raise "card not in hand!"
            else:
                self.hand.remove(cd)
        return cds
    
    # swap the under 
    # returns new under
    def changeUnder(self, originalUnd, newUnd):       
        for cd in originalUnd:
            self.hand.append(cd)
        for cd in newUnd:
            self.hand.remove(cd)
            
        
        
        
        
        
        
        
        
        
        