'''
@author: MattYi, University of Washington
@date: 11/17/2015
'''

from card import *
import player
import deck
import rule
import random
import brainDOS
#import interface

class Game(object):
    '''
    constructor
    playerList, deck, rule, trumpRank, trumpSuit, currentScore, Declarer
    '''
    def __init__(self):
        brain1 = brainDOS.BrainDOS()
        self.pe = player.Player(brain1,0,'MANANXUN')   #east player
        self.pn = player.Player(brain1,1,'WEIWENHUAN')   #north player
        self.pw = player.Player(brain1,2,'ZHUYIZHE')   #west player
        self.ps = player.Player(brain1,3,'TANGSHENQI')   #south player
        self.pe.setNext(self.pn)
        self.pn.setNext(self.pw)
        self.pw.setNext(self.ps)
        self.ps.setNext(self.pe)
        
        self.deck = deck.Deck()
        self.rule = rule.Rule()
        self.trumpRank = '2'
        self.trumpSuit = 'NA'
        self.currScore = 0
        self.declarer = None


        self.rule.setTrumpRank(self.trumpRank)
        #print self.rule.isTrumpAllowed('a')
        
        
    ''' 
    basic functions to set and get variables
    '''
    def setTrumpSuit(self, u):
        pass
        
    def setTrumpRank(self, r):   
        pass
    
    def setDeclarer(self, d):
        pass
    
    
    
    ''' 
    main function
    '''
    
    def on(self):
        #self.start()
        self.deal()
        self.play()
        self.end()
    
    '''
    defines the process of dealing
    '''
            
    def deal(self):
        """
        DESCRIPTION
            Draw cards
        """
        players = [self.pe,self.pn,self.pw,self.ps]
        for i in xrange(25):
            for player in players:
                player.drawCard(self.deck.popCard())
                print "Length of player "+str(player)+"'s current hands:" + str(len(player.hand))
                if self.rule.canDeclareTrump(player.getHand()):
                    cdlist = player.declareTrump(self.declarer,self.trumpRank,self.trumpSuit)
                    while cdlist != False and (not self.rule.isTrumpAllowed(cdlist)):
                        cdlist = player.declareTrump(self.declarer,self.trumpRank,self.trumpSuit)
                    
                    if cdlist != False:
                        self.trumpSuit = cdlist[0].getSuit() 
                        self.declarer = player

        self.deck.bottom = self.declarer.replaceBottom(self.deck.getBottom())
        print "Cards in new bottom:"
        for item in self.deck.bottom:
            print item
        print "Cards in each player's hand:"
        for player in players:
            print str(player)
            for item in player.getHand():
                print item
        print "Cards in declarer's hand:"
        for item in self.declarer.getHand():
            print item
        self.rule.setTrumpSuit(self.trumpSuit)
            #self.pn.drawCard(self.deck.popCard())
            #print "Length of player pn's current hands:" + str(len(self.pn.hand))
            #if self.rule.canDeclareTrump(self.pn.getHand()):
            #    cdlist = self.pn.declareTrump(self.declarer,self.trumpRank,self.trumpSuit)
            #    while cdlist != False:
            #        if self.rule.isTrumpAllowed(cdlist):
            #            self.trumpSuit = cdlist[0].getSuit() 
            #            self.declarer = self.pn
            #        else:
            #            cdlist = self.pn.declareTrump(self.declarer,self.trumpRank,self.trumpSuit)

            #self.pw.drawCard(self.deck.popCard())
            #print "Length of player pw's current hands:" + str(len(self.pw.hand))
            #if self.rule.canDeclareTrump(self.pw.getHand()):
            #    cdlist = self.pw.declareTrump(self.declarer,self.trumpRank,self.trumpSuit)
            #    while cdlist != False:
            #        if self.rule.isTrumpAllowed(cdlist):
            #            self.trumpSuit = cdlist[0].getSuit() 
            #            self.declarer = self.pw
            #        else:
            #            cdlist = self.pw.declareTrump(self.declarer,self.trumpRank,self.trumpSuit)

            #self.ps.drawCard(self.deck.popCard())
            #print "Length of player ps's current hands:" + str(len(self.ps.hand))
            #if self.rule.canDeclareTrump(self.ps.getHand()):
            #    cdlist = self.pw.declareTrump(self.declarer,self.trumpRank,self.trumpSuit)
            #    while cdlist != False:
            #        if self.rule.isTrumpAllowed(cdlist):
            #            self.trumpSuit = cdlist[0].getSuit() 
            #            self.declarer = self.ps
            #        else:
            #            cdlist = self.ps.declareTrump(self.declarer,self.trumpRank,self.trumpSuit)
            
            

    def play(self):
        # initiation
        lastWn = self.declarer
        tmpScore = 0
        self.rule.setTrumpRank(self.trumpRank)
        self.rule.setTrumpSuit(self.trumpSuit)

        while not self.declarer.handIsEmpty():
        # iteration
            lastWnCds = lastWn.declareToPlayCards()
            while not self.rule.isLeadingAllowed(lastWnCds):                
                lastWnCds = lastWn.declareToPlayCards()
            otherPlayerHand = [lastWn.getNext().getHand(),lastWn.getNext().getNext().getHand(),lastWn.getNext().getNext().getNext().getHand()]
            lastWnCds = self.rule.checkLeadingCombo(lastWnCds, otherPlayerHand) 
            lastWnCdSet = self.rule.getCardSet(lastWnCds)
            tmpScore = self.rule.getCardSetScore() 
            
            
            # player 1
            p1 = lastWn.getNext()
            p1Cds = p1.declareToPlayCards([lastWnCds])
            while not self.rule.isFollowingAllowed(p1Cds): 
                p1Cds = p1.declareToPlayCards([lastWnCds])
            p1CdSet = self.rule.getCardSet(p1Cds)
            tmpScore += self.rule.getCardListScore()    
            if self.rule.compareCards(lastWnCdSet, p1CdSet):
                currWn = lastWn
                currWnCdSet = lastWnCdSet
            else:
                currWn = p1
                currWnCdSet = p1CdSet
            
            # player 2
            p2 = p1.getNext()
            p2Cds = p2.declareToPlayCards([lastWnCds, p1Cds])
            while not self.rule.isFollowingAllowed(p2Cds): 
                p2Cds = p2.declareToPlayCards([lastWnCds, p1Cds])
            p2CdSet = self.rule.getCardSet(p2Cds)
            tmpScore += self.rule.getCardSetScore(p2Cds)
            if not self.rule.compareCards(currWnCdSet, p2CdSet):
                currWn = p2
                currWnCdSet = p2CdSet
                
            # player 3
            p3 = p2.getNext()
            p3Cds = p3.declareToPlayCards([lastWnCds, p1Cds, p2Cds])
            while not self.rule.isFollowingAllowed(p3Cds): 
                p3Cds = p3.declareToPlayCards([lastWnCds, p1Cds, p2Cds])
            p3CdSet = self.rule.getCardSet(p3Cds)
            tmpScore += self.rule.getCardSetScore(p3Cds)
            if not self.rule.compareCards(currWnCdSet, p3CdSet):
                currWn = p3
                currWnCdSet = p3CdSet
            
            if currWn == self.declarer or currWn == self.declarer.getNext().getNext():
                self.currScore += tmpScore
            
            # reset the winner and begin next round
            lastWn = currWn
        
        if currWn == self.declarer or currWn == self.declarer.getNext().getNext():
            tmpScore = self.rule.getCardListScore()
            self.currScore += tmpScore
            
                    
        
    
    '''
    set the trump rank, declarer, opponents of the next game
    
    '''
    def end(self, opnPnt):
        pass
    
     
            
            
            
    
        
    
