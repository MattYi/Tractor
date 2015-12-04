'''
@author: MattYi, University of Washington
@date: 11/17/2015
'''
from __builtin__ import False

# This file defines the class of card

class Card(object):
    def __init__(self,cid):        
        #the id of card ranges from 0 to 53
        #the method to convert from id to Card see self.getCard()
        if cid>=0 and cid<=53:
            self.id = cid   
        else:
            raise "wrong card id!"
    
    # tested       
    def getSuit(self):
        if self.getID() == 52:
            return "Black"
        if self.getID() == 53:
            return "Red"
        sList = ["Spade", "Heart", "Club", "Diamond"]
        return sList[self.getID()/13]
    
    # tested
    def getRank(self):
        if self.getID() > 51:
            return "Joker"
        else:
            rList = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
            return rList[self.getID()%13]
    
    # tested               
    def getID(self):
        return self.id
    
    def __str__(self):
        return self.getSuit() + ' ' + self.getRank()
    # tested
    def isTrump(self, tRank, tSuit):
        # input is string
        # if there is no trump suit, tSuit == "None"
        # the implementation ensures that if there is no trump in this game, any tSuit would be OK
        sList = ["Spade", "Heart", "Club", "Diamond"]
        rList = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
        cid = self.getID()
        if cid>51:
            return True
        s = sList[cid/13]
        r = rList[cid%13]
        if s==tSuit or r==tRank:
            return True
        return False
    
    # tested
    def getScore(self):
        if self.getRank() in ['10', 'K']:
            return 10
        if self.getRank() == '5':
            return 5
        return 0
    '''
    # tested   
    def isNext(self, cd, tRank, tSuit):
        s = self.getSuit()
        r = self.getRank()
        rList = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
        rList.remove(tRank)
        if not self.isTrump(tRank, tSuit):
            if s != cd.getSuit():
                return False         
            if rList[-1] == r:
                return False
            return rList[rList.index(r)+1] == cd.getRank()
        if not cd.isTrump(tRank, tSuit):
            return False
        if r in rList:
            if r == rList[-1]:
                return cd.getRank() == tRank and cd.getSuit() != tSuit
            elif cd.getRank() in rList:
                return rList.index(r) + 1 == rList.index(cd.getRank())
            else:
                return False
        if self.getID() == 52:  # self is black joker
            return cd.getID() == 53
        if self.getID() == 53:  # self is red joker
            return False
        if tSuit != "None":  
            if r == tRank and s == tSuit:
                return cd.getID() == 52
            if r == tRank and s!= tSuit:
                return cd.getRank() == tRank and cd.getSuit() == tSuit  
        else:
            if r == tRank:
                return cd.getID() == 52          

    
    # tested
    def compare(self, cd, tRank, tSuit):
        rList = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
        if self.isTrump(tRank, tSuit) and cd.isTrump(tRank, tSuit):
            rList.remove(tRank)
            rList.append(tRank)
            rList.append("Joker")
            if rList.index(self.getRank()) > rList.index(cd.getRank()):
                return 1
            elif rList.index(self.getRank()) < rList.index(cd.getRank()):
                return -1
            else:
                if self.getRank() == tRank:
                    if self.getSuit() == cd.getSuit():
                        return 0
                    elif self.getSuit() == tSuit:
                        return 1
                    else: 
                        return -1
                if self.getRank() == "Joker":
                    if self.getSuit() == cd.getSuit():
                        return 0
                    elif self.getSuit() == "Red":
                        return 1
                    else: 
                        return -1
        
        if (not self.isTrump(tRank, tSuit)) and (not cd.isTrump(tRank, tSuit)):
            if self.getSuit() == cd.getSuit():                
                if rList.index(self.getRank()) > rList.index(cd.getRank()):
                    return 1
                elif rList.index(self.getRank()) < rList.index(cd.getRank()):
                    return -1
                else:
                    return 0
            else:
                raise "different suit, cannot compare!"
        else:
            if self.isTrump(tRank, tSuit):
                return "First is Trump"
            else:
                return "Second is Trump"
    '''      
        
