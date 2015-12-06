from brain import Brain
class BrainTest(Brain):
    def __init__(self,n = 'NoName'):
        super(BrainTest,self).__init__(n)
        self.brainType = 'BrainTest'

    def getType(self):
        return self.brainType

    def declareTrump(self,hand,cardOnDesk):
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
        toPlay = hand[0:4]
        return toPlay

    def changeBottom(self,hand,bottom):
        put = hand[0:2]
        get = bottom[6:]
        print "Cards to be put into the bottom:"
        for item in put:
            print item
        print "Cards wanted from the bottom:"
        for item in get:
            print item
        return [put,get]

        
