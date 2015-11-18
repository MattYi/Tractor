'''
@author: MattYi, University of Washington
@date: 11/17/2015
'''

# This file defines the class of card

class Card(object):
    def __init__(self,cid):        
        #the id of card ranges from 0 to 107
        #the method to convert from id to Card see self.getCard()
        if cid>=0 and cid<108:
            self.id = cid   
        else:
            raise "wrong card id!"
        
    def getCard(self):
        sList = ["spade", "heart", "club", "diamond"]
        rList = ['2','3','4','5','6','7','8','9','10','J','Q','K', 'A']
        cid = self.id
        if cid > 53:
            cid -= 53
        if cid == 52:
            return ['black', 'Joker']
        if cid == 53:
            return ['red', 'Joker']
        s = cid / 13
        r = cid % 13
        return [sList[s], rList[r]]
        
    