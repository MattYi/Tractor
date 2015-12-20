from brain import Brain
class BrainTest(Brain):
    def __init__(self,n = 'NoName'):
        super(BrainTest,self).__init__(n)
        self.__brainType = 'BrainTest'

    def getType(self):
        return self.__brainType

    def declareTrump(self,hand,cardOnDesk):
        """
        Description:
            If want to declare trump, it should return a list of cards used to declare. Otherwise, return False

        Arguments:
            -hand is a list of card objects
            -cardOnDesk is a list. E.g. if this player is the last to play cards in this round, 
                cardOnDesk = [[cards played by p1 this round],[cards played by p2 this round],[cards played by p3 this round]]

        Return:
            If want to declare trump, return a list of card object shown to Game and Game will check if they are valid
            If do not want to declare trump, return False
        """
        #test declare trump with one card
        print "declareTrump() in BrainTest was called."
        c1=[hand[0],hand[1]]
        print "Will return These cards from declareTrump():"
        for item in c1:
            print item 
        return c1

        #test declare trump with more than one card
        #TODO 
        #test not to declare trump
        #TODO 

    def declareToPlayCards(self,hand,cardOnDesk):
        """
        Description:
        Arguments:
            -hand is a list of card objects
            -cardOnDesk is a list. E.g. if this player is the last to play cards in this round, 
                cardOnDesk = [[cards played by p1 this round],[cards played by p2 this round],[cards played by p3 this round]]
        Return:
            Should return a list of card objects
        """
        toPlay = hand[0:4]
        return toPlay

    def changeBottom(self,hand,bottom):
        """
        Description:
            The player will return a list of 8 cards that will be put into the bottom
        Arguments:
            -bottom is a copy of list of cards that are the same as current bottom cards
            -hand is hand card of this player
        Return:
            This function will return [put,get]
            -put is a list of cards to be put into the bottom
            -get is a list of cards that the player want from the bottom
        """
        put = hand[0:2]
        get = bottom[6:]
        print "Cards to be put into the bottom:"
        for item in put:
            print item
        print "Cards wanted from the bottom:"
        for item in get:
            print item
        return [put,get]

        
