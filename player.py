'''
@author: MattYi, University of Washington
@date: 11/17/2015
'''
from card import *

class Player(object):
    def __init__(self, pid = -1, n = "NoName"):
        #to do: it seems good to implement the player as a node of a linked list
        #therefore please add self.next in constructor where the next points at the next player
        #it does not need to be initialized here in the constructor
        #correspondingly, a function setNext() and getNext() are needed
        pass
    
    def setNext(self):
        pass
    
    def getNext(self):
        pass
        
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
    
    def pickCards(self):
    #TODO: returns the card that the player wants to play
        pass
    
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
            
        
        
        
        
        
        
        
        
        
        