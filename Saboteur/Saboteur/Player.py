# -*- coding: utf-8 -*-
"""
Created on Sun Dec 25 12:13:24 2022

@author: 22044
"""

from abc import abstractmethod,ABC 

class Player(ABC):
    def __init__(self,name,order,identify):
        # Name of Player
        self.name = name
        # Identify of Player
        self.identify = identify
        # Order of Player
        self.order = order
        self.HandCards = []
        # Status of Tools
        self.Light = True
        self.Pike = True
        self.Wagon = True
        # Gold 
        self.gold = 0
    
    @abstractmethod
    def Usecard(self):
        pass
    
    # Distribute m cards for every player    
    def DistributeCards(self,deck,NumberHandCards):        
        self.HandCards = deck[:NumberHandCards]
        del deck[:NumberHandCards]        
        return
    
    def GetCard(self,deck):
        self.HandCards.append(deck[0])
        del deck[:1]
        return
    
    
    def Initial(self,identify):
        # Identify of Player
        self.identify = identify
        self.HandCards = []
        # Status of Tools
        self.Light = True
        self.Pike = True
        self.Wagon = True
    
    
    def DelCard(self,CardChoice):
        del self.HandCards[CardChoice] 
        