class Brain(object):
    def __init__(self, n = 'NoName'):
        """
        data member:
            int id
            string name
        This is a base virtual class to be inherited by other classes like BrainDOS, AI, UI
        It is called by Player class
        """
        self.__name = n

    def getName(self):
        return self.__name

    def declareTrump(self,hand,cardOnDesk):
        """
        Description:
            INTERFACE, TO BE IMPLEMENTED BY ITS DERIVED CLASS.
            If want to declare trump, it should return a list of cards used to declare. Otherwise, return False

        Arguments:
            -hand is a list of card objects
            -cardOnDesk is a list. E.g. if this player is the last to play cards in this round, 
                cardOnDesk = [[cards played by p1 this round],[cards played by p2 this round],[cards played by p3 this round]]

        Return:
            If want to declare trump, return a list of card object shown to Game and Game will check if they are valid
            If do not want to declare trump, return False
        """
        pass

    def declareToPlayCards(self,hand,cardOnDesk):
        """
        Description:
            INTERFACE, TO BE IMPLEMENTED BY ITS DERIVED CLASS.
        Arguments:
            -hand is a list of card objects
            -cardOnDesk is a list. E.g. if this player is the last to play cards in this round, 
                cardOnDesk = [[cards played by p1 this round],[cards played by p2 this round],[cards played by p3 this round]]
        Return:
            Should return a list of card objects
        """
        pass

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
        pass

