'''
@author: MattYi, University of Washington
@date: 11/17/2015
'''

from card import *
import player
import deck
import rule
import random

class game(object):
    '''
    constructor
    playerList, deck, rule, trumpRank, trumpSuit, currentScore, Declarer
    '''
    def __init__(self):
        
        
        
        self.deck = deck.Deck()
        self.rule = rule.Rule()
        self.trumpRank = '2'
        self.trumpSuit = 'NA'
        self.currScore = 0
        self.declarer = None
        self.upDeclarer = None
        self.dnDeclarer = None
        self.opDeclarer = None
        
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
        self.start()
        self.deal()
        self.end()
    
    '''
    defines the process of dealing
    '''
            
    def deal(self):
        self.deck.shuffle()
        if self.declarer == None:
            p = random.randint(0,3)
        while deck.nRemaining() != 0:
            cd = deck.popCard()
            self.players[p].getCard(cd)
            if (rule.canSetTrumpSuit(self.players[p])):
                self.players[p].setTrumpSuit()
                
            p = (p + 1) % 4
            
            

    def play(self):
        currWn = Declarer
        
    
    '''
    set the trump rank, declarer, opponents of the next game
    
    '''
    def end(self, opnPnt):
        pass
    
     
            
            
            
    
        
    
