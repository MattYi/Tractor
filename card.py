'''
@author: MattYi, University of Washington
@date: 11/17/2015
'''
from __builtin__ import False

#test fork
# This file defines the class of card

class Card(object):
    def __init__(self,cid):        
        #the id of card ranges from 0 to 107
        #the method to convert from id to Card see self.getCard()
        if cid>=0 and cid<=53:
            self.id = cid   
        else:
            raise "wrong card id!"
            
    def getSuit(self):
        if self.getID() == 52:
            return "Black"
        if self.getID() == 53:
            return "Red"
        sList = ["Spade", "Heart", "Club", "Diamond"]
        return sList[self.getID()/13]
    
    def getRank(self):
        if self.getID() > 51:
            return "Joker"
        else:
            rList = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
            return rList[self.getID()%13]
                    
    def getID(self):
        return self.id
    
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
    
    def getScore(self):
        if self.getRank() in ['10', 'K']:
            return 10
        if self.getRank() == '5':
            return 5
        
    def isNext(self, cd, tRank, tSuit):
        s = self.getSuit()
        r = self.getRank()
        rList = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
        if not self.isTrump(tRank, tSuit):
            rList.remove()
            if s == cd.getSuit():
                tmp = rList.index(r)
                if tmp == 12:
                    return False
                if tmp + 1 == tRank:
                    tmp += 1
                    if tmp == 12:
                        return False
                if rList[tmp] == cd.getRank():
                    return True
        if self.getSuit() == "Red": # The first card is Red Joker
            return False
        if self.getSuit() == "Black": # The first card is Black Joker
            return cd.getSuit() == "Red"
        if self.getSuit() == tSuit and self.getRank() == tRank: # The first card is Trump Suit Rank
            return cd.getSuit() == "Black"
        if self.getSuit() != tSuit and self.getRank() == tRank: # The first card is Trump Rank
            return cd.getSuit() == tSuit and cd.getRank() == tRank
        tmp = rList.index(self.getRank())
        if rList[tmp + 1] == tRank:
            tmp += 1
            if tmp == cd.getRank():
                return True
            else:
                return False
      
    def __str__(self):
        return self.getSuit() + ' ' + self.getRank()

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
           
        
