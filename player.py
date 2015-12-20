'''
@author: MattYi, University of Washington
@date: 11/17/2015
'''
from card import Card
from deck import Deck
import sys
import pdb

class Player(object):
    def __init__(self, brain, pid = -1, n = "NoName"):
        """
        data member:
            int id
            list hand
            string name
            Brain brain

        Brain is the base class for some classes like AI, UI, DOS
        Objects of this class and their functions are designed to be called by Game object on server instead of by each of the 4 threads on client.
        """


    # id: from 0 to 3, since currently we only consider the situation that there are 4 players
        self.id = pid
        self.name = n
    # hand: it is a list of card object that this player is holding
        self.hand = []
        self.brain = brain
        self.next = None

    
    def setNext(self, nextPlayer):
        self.next = nextPlayer
    
    def getNext(self):
        return self.next
        
    def setName(self, n):
        self.name = n
        
    def getName(self, n):
        return self.name
    
    def setID(self,pid):
        if pid<0  or pid>3:
            print "Try to set a invalid player id. Valid ID shoulb be in the range of 0 to 3"
            sys.exit()
        self.id = pid
    
    def getID(self):
        return self.id

    def __str__(self):
        return "[ Player ID: " + str(self.id) + ". Name: " + str(self.name) + ". Brain type: " + self.brain.getType() + " ]"

    
    def displayHands(self):
        for item in self.hand:
            print item
    
    def handIsEmpty(self):
        """
        Check if a player's hands are empty 
        """
        if self.hand:
            return False
        else:
            return True
    
    # add the card to the self.hand
    def drawCard(self, cd):
        """
        If cd is not a Card object, TypeError will be raised
        """
        if type(cd) == Card:
            self.hand.append(cd)
            return True
        else:
            raise TypeError("Try to append a object to Hands which is not a Card object")
            return False
    
    def declareTrump(self,cardOnDesk):
        """
        DESCRIPTION:
            Currently, this function will be called in Game object each time a player draw a card.
            If this player want to declare trump, it return the a card object and delcare suit of of it to be trump 
            Otherwise it will return False
        ARGUMENTS:
            -cardOnDesk is a list. E.g. if this player is the last to play cards in this round,
            cardOnDesk = [[cards played by p1 this round],[cards played by p2 this round],[cards played by p3 this round]]
        RETURN:
            If want to declare trump, return a list of card object shown to Game and Game will check if they are valid
            If do not want to declare trump, return False
        """
        #cds should be a list of one card or two cards (declare after someone has already done this)
        cds = self.brain.declareTrump(self.hand,cardOnDesk)
        if cds == False:#Not declare
            return False
        else:#declare trump
            #check if those cards are valid
            for cd in cds:
                if type(cd) == Card and ( cd in self.hand ):
                    continue
                else:
                    print "Player, "+self.name+", tried to play a card not in his hand: "+str(cd)
                    raise TypeError("Try to return a object which is not a Card object")

            print "In player.declareTrump():"
            print "Player, "+self.name+" declared Trump using: "
            for cd in cds:
                print cd
            return cds
    

    def declareToPlayCards(self,cardOnDesk):
        """
        DESCRIPTION:
            Game will call this function to request a list of cards this player try to play (But these cards won't be deleted from self.hand yet).

        ARGUMENTS:
            -cardOnDesk is a list. E.g. if this player is the last to play cards in this round, 
                cardOnDesk = [[cards played by p1 this round],[cards played by p2 this round],[cards played by p3 this round]]

        RETURN:
            Return a list of card objects that this player try to play.
        """
        #cds is a list of card objects
        cds = self.brain.declareToPlayCards(self.hand,cardOnDesk)
        if type(cds) != list: #check if cds is a list
            raise TypeError("Object to be returned is not a list")
        else:
            for cd in cds:
                if type(cd) != Card: #check if try to return a list of Card object.
                    raise TypeError("Objects in the list are not all Card objects")
                else:
                    if cd not in self.hand: #check if all cards it want to play are in self.hand
                        raise "card not in hand!"
        return cds

    def playCards(self,cards):
        """
        Game can delete some cards from self.hand by calling this method, which represents the process of a player playing some cards.
        -cards is a list of cards that will be deleted from self.hand
        It has no return value.
        """
        for item in cards:
            if item in self.hand:
                self.hand.remove(item)
    
    def replaceBottom(self, bottom):       
        """
        DESCRIPTION:
            Game will call this function to ask this player if it want to change the bottom cards
        ARGUMENTS:
            -bottom is a copy of list of cards that are the same as current bottom cards
        RETURN:
            The player will return a list of 8 cards that will be put into the bottom
            If anything went wrong in this function, it will return False
        """
        #put is a list of cards to be put into the bottom
        #get is a list of cards that the player want from the bottom
        [put,get] = self.brain.changeBottom(self.hand,bottom)
        #check if put and get have the same length
        if len(put) != len(get):
            print "Number of cards requested from the bottom is not the same as that of cards to be put back."
            return False
        #check if cards in put are all in self.hand
        for item in put:
            if item not in self.hand:
                print "Try to put card, "+str(item)+" into the bottom card, which is not in Hands"
                return False
        #check if cards in get are all in bottom
        for item in get:
            if item not in bottom:
                print "Requested card, "+str(item)+" from the bottom card, which is not in the bottom"
                return False
        #If all the checks above are approved, return a list of 8 cards to be put into deck.bottom
        from copy import deepcopy
        newBottom = deepcopy(bottom) #deep copy bottom in case we accidently modify bottom
        for [p,g] in zip(put,get):
            #print "put: "+ str(p) + "id: " + str(id(p))
            #print "get: "+ str(g) + "id: " + str(id(g))
            #print "newBottom at this moment:"
            #for item in newBottom:
            #    print str(item) + "id: " + str(id(item))
            self.hand.remove(p)
            self.hand.append(g)
            newBottom.remove(g)
            newBottom.append(p)
        return newBottom




            
        
        
        
        
        
        
        
        
        
        
