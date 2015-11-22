'''
@author: MattYi, University of Washington
@date: 11/17/2015
'''

# whole file tested


'''
This file defines how at a time cards can be played:
Basic type: Single Card or Tract
Actural type: CardType, complex of single cards and Tracts
'''
from card import *

# tested
'''
the class of single card
stores the card inside
'''

class singleCard(object):
    def __init__(self, cd):
        self.card = cd
        
    def __str__(self):
        return self.card.__str__()

# tested
'''
the class of tract
stores the smallest card and the length of the tract
'''
    
class tract(object):
    def __init__(self,cd, l):
        # e.g. a tract like "2233" is 
        self.card = cd
        self.length = l
    
    def getCard(self):
        return self.card
    
    def getLength(self):
        return self.length
        
    def __str__(self):
        return self.card.__str__() + ' ' + str(self.length)

'''
the class of a set of cards that is played at a time
stores two list inside
'''
            
class cardSet():
    def __init__(self, scList, tList):
        self.singleCardList = scList
        self.tractList = tList
    
    '''
    -> bool
    return 1 if the cardset is a combol (combination of singlecard(s) and(or) tract(s)
    return 0 otherwise
    '''          
    def isCombol(self):
        if len(self.singleCardList) + len(self.tractList) > 1:
            return True
        return False
    
    '''
    -> bool
    return 1 if the cardset is ONLY ONE single card
    return 0 otherwise
    '''  
    def isSingleCard(self):
        if len(self.singleCardList) == 1 and len(self.tractList) == 0:
            return True
        return False 
    
    '''
    -> bool
    return 1 if the cardset is ONLY ONE tract
    return 0 otherwise
    '''   
    def isTract(self):
        if len(self.singleCardList) == 0 and len(self.tractList) == 1:
            return True
        return False 
    
    '''
    returns a list like [a, b1, b2, b3, ... bn]
    a means number of singles
    bi means the length of ith tract
    '''
    def getType(self):
        t = []
        t.append(len(self.singleCardList))
        for i in self.tract:
            t.append(i.getLength())
        return t
      
    def __str__(self):
        if self.isSingleCard():
            return 'SingleCard: ' + self.singleCardList[0].__str__()
        if self.isTract():
            return 'Tract: ' + self.tractList[0].__str__()
        if self.isCombol():
            tmp = ['SingleCards:']
            for sc in self.singleCardList:
                tmp.append(sc.__str__())
            tmp1 = ' '.join(tmp)
            tmp = ['Tract:']
            for t in self.tractList:
                tmp.append(t.__str__())
            tmp2 = ' '.join(tmp)
            return tmp1 + ' ' + tmp2
        
            
    
        
        
        
        
        
        
        