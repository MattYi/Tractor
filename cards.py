'''
@author: MattYi, University of Washington
@date: 11/17/2015
'''

# This file defines the class of card

class Card(object):
    def __init__(self,s,r):
        sList = ["spade", "heart", "club", "diamond", "red", "black"]
        rList = ['1','2','3','4','5','6','7','8','9','10','J','Q','K','Joker']
        if "NoProblemMet":
            self.suit = sList[s]
            self.rank = rList[r]
        
        
