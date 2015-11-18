'''
@author: MattYi, University of Washington
@date: 11/17/2015
'''

from card import *
from player import *
from deck import *

class game(object):
    def __init__(self):
        self.players = []
        self.declarer = -1
        self.opponent = [-1,-1]
        self.opdec = -1
        self.deck = Deck()
        self.trumpRank = ""
    
    ''' 
    basic functions to set and get variables
    '''
    def setTrumpUnit(self, u):
        pass
        
    def setTrumpRank(self, r):   
        pass
    
    def setDeclarer(self, d):
        pass
    
    def getDeclarer(self):
        return self.declarer
    
    ''' 
    main function
    '''
    
    def on(self):
        self.start()
        self.deal()
        self.end()
    
    # nm is a list of 4, for initializing the names of players  
    # currently haven't thought about anything else needed to be initialized 
    def start(self, nm):
        for i in xrange(4):
            game.players.append(Player(i, nm[i]))
        
    def deal(self):
        game.deck.shuffle()
        fd = 0  # it should be random number in 0 to 3, denoting the first one to draw a card
        count = 108 # remaining cards in the deck
        tmptrump = "" # the unit of the rank
        while count > 8:
            self.players[fd].getCard(self.deck.popCard())
            tmptrump = self.players[fd].setTrump()
            fd = (fd + 1)%4
            count -= 1
        self.setTrumpUnit(tmptrump)
    
    '''
    The following are the auxilary functions needed in self.play()
    '''
    
    def checkCards(self, fcds): #check if the what the player played is consistant with the rule
        pass
    
    def compCards(self, playerID1, cds1, playerID2=-1, cds2=""): # compare the cards that two players played
        pass
    
    def calcPoints(self, cds):  # return the total score in the cards
        pass
    
    def calcOpponentPoints(self):  # return the opponents points in this round
        pass
    
    def play(self):
        fp = self.getDeclarer() #the first one the play a card
        count = 4
        currPnt = 0
        currOpnPnt = 0
        currWnr = -1
        while !self.players[fp].emptyHand():
            while count>0:
                cds = self.players[fp].playCard()
                currPnt += self.calcPoints(cds)
                currWnr = compCards()
            currOpnPnt += self.calcOpponentPoints()
        '''
        here goes the way to deal with the Under
        '''
        return currOpnPnt
    
    '''
    set the trump rank, declarer, opponents of the next game
    
    '''
    def end(self, opnPnt):
        pass
    
     
            
            
            
    
        
    
