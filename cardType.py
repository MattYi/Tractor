'''
@author: MattYi, University of Washington
@date: 11/17/2015
'''

'''
This file defines how at a time cards can be played:
Basic type: Single Card or Tract
Actural type: CardType, complex of single cards and Tracts
'''
from card import *

class SingleCard(object):
    def __init__(self, cd):
        self.card = cd
        
    def __gt__(self, sc2):
        return self.card > sc2.card
    
    def __lt__(self, sc2):
        return self.card < sc2.card
    
    def __eq__(self, sc2):
        return self.card == sc2.card


class Tract(object):
    def __init__(self,cd, l):
        # e.g. a tract like "2233" is 
        self.card = cd
        self.length = l
    
    def __gt__(self, sc2):
        if self.length == sc2.length:
            return self.card > sc2.card
        else:
            raise "Different Tract Length!"
        
    def __lt__(self, sc2):
        if self.length == sc2.length:
            return self.card < sc2.card
        else:
            raise "Different Tract Length!"
    
    def __eq__(self, sc2):
        if self.length == sc2.length:
            return self.card == sc2.card
        else:
            raise "Different Tract Length!"
     
        
class CardSet():
    def __init__(self, cardList, tRank, tSuit):
        self.singlecardList = []
        self.tractList = []
        self.isDrop = 0     #The cards is dropped if self.isDrop == 1
        cardList.sort(key=lambda cd: cd.id)
        
        
        l = len(cardList)
        if l==0:
            raise "Empty Input List!"
        if l==1:
            self.singlecardList.append(cardList[0])
            return
        tmpList = []
        for i in xrange(l-1):
            if cardList[i+1] == cardList[i]:
                tmpList.append(cardList[i])
                i += 1;
            else:
                self.singlecardList.append(cardList[i])
        i = 0
        while i < len(tmpList)
            tmpL = 1
            
        
            
        
        
        
        
        
        