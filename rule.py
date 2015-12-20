'''
This class keeps the rules of tractor
'''

import sys
import cardSet
from __builtin__ import False

class Rule(object):
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
    Bellow are the rules for the object card or a list of the object card:
    isTrump()
    getCardScore()
    getCardListScore()
    compareCards(cd1, cd2)
    rearrange(cdlist)
    getCardSet()
    '''
    
    '''
    card->bool
    return 1 if the card is trump
    return 0 if not
    '''   
    def isTrump(self, cd):
        s = cd.getSuit()
        r = cd.getRank()
        if s == self.trumpSuit or r == self.trumpRank or r == "Joker":
            return 1
        return 0
    
    '''
    card -> int
    return the score of the card
    return 0, 5, 10 for different cards
    '''
    def getCardScore(self, cd):
        r = cd.getRank()
        if r == '5':
            return 5
        if r == '10' or r == 'K':
            return 10
        return 0
    
    def getCardListScore(self, cdList):
        tmpScore = 0
        for cd in cdList:
            tmpScore += self.getCardScore(cd)
        return tmpScore
    
    '''
    card -> int
    this is an auxiliary method 
    to sort the cards, find the next one and compare two cards
    '''
    
    # well tested
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
    
    '''
    cd, cd -> int
    compare two cards
    the former one is larger return 1
    the latter one is larger return -1
    same card: return 0
    '''
                    
    # well tested
    def compareCards(self, cd1, cd2):
        pnt1 = self.getCardPnt(cd1)
        pnt2 = self.getCardPnt(cd2)
        if pnt1 > pnt2:
            return 1
        if pnt1 == pnt2:
            return 0
        return -1
    '''
    list(card) -> void
    an auxiliary method to reaarange cards in a list
    according to: self.getCardPnt(cd)
    if same, according to there suit(or id)
    '''
    # well tested 
    def rearrange(self, cdList):
        cdList.sort(key=lambda cd: cd.id)
        cdList.sort(key=lambda cd: self.getCardPnt(cd))
        return cdList
    
    '''
    list(card) -> bool
    return 1 if the card list is dropped
    '''
    
    # well tested  
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
                        
    '''
    construct an instance of class cardSet
    '''
    
    # well tested              
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
    
    '''
    cardSet, cardSet -> bool
    the former one should be played first
    return 1 if former one is larger
    return 0 otherwise
    '''
    
    # well tested   
    def compareCardSet(self, cs1, cs2): 
        if cs2.isDrop():  
            return True
        if not cs1.getType() == cs2.getType():
            return True
        sc1 = cs1.getSingleCardList()
        sc2 = cs2.getSingleCardList()
        scLen = len(sc1)
        for i in xrange(scLen):
            if self.compareCards(sc1[i], sc2[i]) >= 0:
                return True
        t1 = cs1.getTractList()
        t2 = cs2.getTractList()
        tLen = len(t1)
        for i in xrange(tLen):
            if self.compareCards(t1[i][0],t2[i][0]) >= 0:
                return True
        return False
                
    
    '''
    bellow are the rules during the process of dealing
    '''
    
    
    
    
    # not implemented yet
    def canSetTrumpSuit(self, p):
        pass                
    
    
    '''
    bellow are the rules during the process of playding
    isLeadingAllowed()    if the leading player can play the cards
    *need test* checkLeadingCombo() check if the player need to play smaller cards due to failed combo
    *need test for multi tracts* isFollowingAllowed() check what the follower played is allowed
        *assistant methods* cardListContainTract
        *assistant methods* searchTractTrump
        *assistant methods* searchTractSuit
    '''

    def isLeadingAllowed(self, cdList):               
        '''
        whether the player is allowed to play the cards
        '''
        return not self.isDrop(cdList)
       
    
    def checkLeadingCombo(self, leadingCards, otherPlayerHand):
        
        '''
        whether the player can play this combo
        '''
        flag = 1
        cdset = self.getCardSet(leadingCards)
        scList = cdset.getSingleCardList()
        if not scList.empty():
            tgtcd = scList[0]
            for playerHand in otherPlayerHand:
                if flag == 0:
                    break
                for cd in playerHand:
                    if self.isTrump(cd) and self.isTrump(tgtcd) and self.compareCards(cd, tgtcd)>0:
                        flag = 0
                        break
                    if not self.isTrump(cd) and self.isTrump(tgtcd) and cd.getSuit()==tgtcd.getSuit() and self.compareCards(cd, tgtcd)>0:
                        flag = 0
                        break
                '''
                to here it is made sure that no other player has larger single card than leading player
                '''
        if flag == 1:
            tList = cdset.getTractList()
            if not tList.empty():
                for t in tList:
                    if flag == 0:
                        break
                    for playerHand in otherPlayerHand:
                        playerHand = self.rearrange(playerHand)
                        altCardList = []
                        if self.isTrump(t.getCard()):
                            for cd in playerHand:
                                if self.isTrump(cd):
                                    altCardList.append(cd)
                        else:
                            for cd in playerHand:
                                if cd.getSuit() == t.getCard().getSuit():
                                    altCardList.append(cd)
                        altCardSet = self.getCardSet(altCardList)
                        altTList = altCardSet.getTractList()
                        if not altTList.empty():   
                            for altT in altTList():
                                if altT.getLength() == t.getLength() and self.compare(altT.getCard(), t.getCard()):
                                    flag = 0
                                    break
        
        if flag == 1:
            return leadingCards
        else:
            if not cdset.getSingleCardList().empty():
                return cdset.getSingleCardList()[0]
            else:
                return cdset.getTractList()[0]                        
            '''
            to here it is made sure that no other player has larger tractor than leading player
            '''    

    
    
    # well tested
    def cardListContainTract(self,cdList,tLength):
        if tLength == 0 and len(cdList)>0:
            return True
        for i in xrange(len(cdList)-tLength):
            for j in xrange(2*tLength):
                if self.getCardPnt(cdList[j]) - self.getCardPnt(cdList[i]) != (j - i)/2:
                    break
            return True
        return False   
        
    
    
    
    '''
    if leading is a tract: well tested
    if leading is a singleCards: well tested
    if leading is multi tracts: not tested yet
    if leading contains both singleCards and multi tracts: not tested yet
    '''
    
    
    def isFollowingAllowed(self, leadingCds, followingCds, followingHand):
        leadingCardSet = self.getCardSet(leadingCds)
        lenSingleCards = len(leadingCardSet.getSingleCardList())
        lenTract = len(leadingCardSet.getTractList())
        copyFollowingCards = followingCds[:]
        copyFollowingHand = followingHand[:]
        flag = None #flag == 1 legal, 0 illegal
        if lenTract!=0:
            # leading contains tracts
            for tract in leadingCardSet.getTractList():
                if self.isTrump(leadingCds[0]):
                    flag = self.searchTractTrump(copyFollowingHand, copyFollowingCards, tract.getLength())
                else:
                    suit = leadingCds[0].getSuit()
                    flag =  self.searchTractTrump(copyFollowingHand, copyFollowingCards, suit, tract.getLength())
        
        if flag == False:
            return flag
        
        elif lenSingleCards != 0:
            # leading contains single cards
            tmpFollowingHand = []
            tmpFollowingCds = []
            if self.isTrump(leadingCds[0]):
                for cd in copyFollowingCards:
                    if self.isTrump(cd):
                        tmpFollowingCds.append(cd)
                for cd in copyFollowingHand:
                    if self.isTrump(cd):
                        tmpFollowingHand.append(cd)
            else:
                suit = leadingCds[0].getSuit()
                for cd in copyFollowingCards:
                    if not self.isTrump(cd) and cd.getSuit()==suit:
                        tmpFollowingCds.append(cd)
                for cd in copyFollowingHand:
                    if not self.isTrump(cd) and cd.getSuit()==suit:
                        tmpFollowingHand.append(cd)
            return len(tmpFollowingCds) == min(len(tmpFollowingHand), len(leadingCds))   
    
    
    def searchTractTrump(self, hand, ctp, delta):
        #calculate lm, the length of the tract with the largest length in follower's hand
        tmpHand = []
        for cd in hand:
            if self.isTrump(cd):
                tmpHand.append(cd)
        tmpHandCdSet = self.getCardSet(tmpHand)
        if len(tmpHandCdSet.getTractList())==0:
            lm = 0
        else:
            lm = tmpHandCdSet.getTractList()[-1].getLength()
        # get the ctp with same suit or with target
        tmpCtp = []
        for cd in ctp:
            if self.isTrump(cd):
                tmpCtp.append(cd)    
        tmpCtpSet = self.getCardSet(tmpCtp)
        # termination of recursion
        delta -= lm
        if delta == 0:
            return True
        elif delta>0 and lm==0:
            nHandSuit = len(tmpHand)    # not implemented yet
            if len(tmpCtp) == min(2*delta, nHandSuit):
                return True
            else:
                return False
        # 
        tmpT = None
        for t in tmpCtpSet.getTractList():
            if t.getLength() == lm:                 
                tmpT = t
                break
        # if the player played the card required
        if tmpT!=None:
            for cd in t.getCardList():
                ctp.remove(cd)
                hand.remove(cd)
        else:
            return False
        return self.searchTractTrump(hand, ctp, delta)
    
    
    def searchTractSuit(self, hand, ctp, suit, delta):
        #calculate lm, the length of the tract with the largest length in follower's hand
        tmpHand = []
        for cd in hand:
            if not self.isTrump(cd) and cd.getSuit()==suit:
                tmpHand.append(cd)
        tmpHandCdSet = self.getCardSet(tmpHand)
        if len(tmpHandCdSet.getTractList()==0):
            lm = 0
        else:
            lm = tmpHandCdSet.getTractList()[-1].getLength()
        # get the ctp with same suit or with target
        tmpCtp = []
        for cd in ctp:
            if not self.isTrump(cd) and cd.getSuit() == suit:
                tmpCtp.append(cd)    
        tmpCtpSet = self.getCardSet(tmpCtp)
        # termination of recursion
        delta -= lm
        if delta == 0:
            return True
        elif delta>0 and lm==0:
            nHandSuit = len(tmpHand)    # not implemented yet
            if len(tmpCtp) == min(2*delta, nHandSuit):
                return True
            else:
                return False
        # 
        tmpT = None
        for t in tmpCtpSet.getTractList():
            if t.getLength() == lm:                 
                tmpT = t
        # if the player played the card required
        if tmpT!=None:
            for cd in t.getCardList():
                ctp.pop(cd)
                hand.pop(cd)
        else:
            return False
        return self.searchTract(self, hand, ctp, delta)
    
    
    
        
    
               
    
        
            
            