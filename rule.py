'''
This class keeps the rules of tractor
'''

import sys
import cardSet

class rule(object):
    def __init__(self):
        self.trumpRank = 'NA'
        self.trumpSuit = 'NA'
        
    def setTrumpRank(self, tR):
        self.trumpRank = tR
        
    def setTrumpSuit(self, tS):
        self.trumpSuit = tS
        
    def getTrumpRank(self):
        return self.trumpRank
    
    def getTrumpSuit(self):
        return self.trumpSuit
    
    '''
    return 1 if the card is trump
    return 0 if not
    '''   
    def isTrump(self, cd):
        s = cd.getSuit()
        r = cd.getRank()
        if s == self.trumpSuit or r == self.trumpRank or r == "Joker":
            return 1
        return 0
    
    def getCardScore(self, cd):
        r = cd.getRank()
        if r == '5':
            return 5
        if r == '10' or r == 'K':
            return 10
        return 0
    
    def getCardPnt(self, cd):
        r = cd.getRank()
        s = cd.getSuit()
        rList = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']  
        rList.remove(self.trumpRank) 
        if self.trumpSuit == 'None':
            if not self.isTrump(cd):
                try: 
                    return rList.index(r)
                except:
                    print 'No such rank!'
                    sys.exit(1)
            else:
                if r == self.trumpRank:
                    return 100
                if r == 'Joker' and s == 'Red':
                    return 102
                if r == 'Joker' and s == 'Black':
                    return 101
                print 'No such rank!'
                sys.exit()                        
        else:
            if not self.isTrump(cd):
                try: 
                    return rList.index(r)
                except:
                    print 'No such rank!'
                    sys.exit(1)
            else:
                try: 
                    return rList.index(r)+100
                except:
                    if r == self.trumpRank and s == self.trumpSuit:
                        return 113
                    if r == self.trumpRank and s != self.trumpSuit:
                        return 112
                    if r == 'Joker' and s == 'Red':
                        return 115
                    if r == 'Joker' and s == 'Black':
                        return 114
                    print 'No such rank!'
                    sys.exit()     
        
    def rearrange(self, cdList):
        cdList.sort(key=lambda cd: cd.id)
        cdList.sort(key=lambda cd: self.getCardPnt(cd))
        return cdList
        
    def isDrop(self, cdList):
        s = cdList[0].getSuit()
        isT = self.isTrump(cdList[0])
        for cd in cdList:
            if self.isTrump(cd) != isT:
                return True
        if isT:
            return False
        for cd in cdList:
            if cd.getSuit() != s:
                return True
        return False
                        
                    
    def getCardSet(self, cdList):   
        if self.isDrop(cdList):
            return []
        cdList = self.rearrange(cdList)
        length = len(cdList)
        if length == 1:
            return cardSet.cardSet(cdList, [])
        ind = 1
        singleCard = []
        doubleCard = []
        while ind < length:
            while ind < length and self.getCardPnt(cdList[ind])==self.getCardPnt(cdList[ind-1]):
                doubleCard.append(cdList[ind])
                ind += 2
            if ind == length + 1:    
                pass
            elif ind == length:
                singleCard.append(cdList[length-1])
            else:
                singleCard.append(cdList[ind-1])
                ind += 1
        length = len(doubleCard)
        ind = 1
        tmp = []
        tr = []
        while ind < length:
            while ind < length and self.getCardPnt(doubleCard[ind]) == self.getCardPnt(doubleCard[ind-1]) + 1:
                tmp.append(doubleCard[ind-1])
                ind += 1
            tmp.append(doubleCard[ind-1])
            tr.append(cardSet.tract(tmp[0], len(tmp)))
            ind += 1
        if ind == length:
            tr.append(cardSet.tract(doubleCard[length-1],1))
        
        tr.sort(key=lambda t:self.getCardPnt(t.getCard()))
        tr.sort(key=lambda t:t.getLength())
        return cardSet.cardSet(singleCard, tr)
       
    def compareCardSet(self, cs1, cs2):   
        if cs1.getType() == cs2.getType():
            pass
                    
                    
                    
            
            
            
            