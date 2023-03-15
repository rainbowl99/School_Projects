# -*- coding: utf-8 -*-
"""
Created on Sun Dec 25 22:31:41 2022

@author: 22044
"""

from Player import Player
from Cards import Cards
from Map import Map
import random

class Robot(Player):
    
    def __init__(self,name,order,identify):
        super().__init__(name,order,identify)
        self.map_use = 0
        self.tab_choice = [0,1,2]
        
    def PrintHandCards(self,HandCards):
        print(f"You are : {self.identify}")
        print("Your HandCards are : ")
        res1 = res2 = res3 = ''
        i = 0
        for card in HandCards:
            i += 1
            res1 += f"    {card[0]}  "
            res2 += f"{i}:  {card[1]}, "
            res3 += f"    {card[2]}  "
        
        res2 += f"{i+1}:  Throw away a card."
        print(res1)
        print(res2)
        print(res3)
        
    def Usecard(self,Map,player,GoldPlace):       
        # Print the status of tools
        Tools_Have = "The tools you have now: "
        Tools_DontHave = "You do not have the tools : "
        print("------------------------------------------------------------------------------------")
        print("Status of Tools:")
        if self.Light == False and self.Pike == False and self.Wagon == False:
            print("You don't have any tools right now.")
        else:
            if self.Light == False:
                Tools_DontHave += "Light; "     
            else:
                Tools_Have += "Light; "
                
            if self.Pike == False:
                Tools_DontHave += "Pile; "      
            else:
                Tools_Have += "Pike; "
                
            if self.Wagon == False:
                Tools_DontHave += " Wagon; "
            else:
                Tools_Have += "Wagon; "
                
            Tools_DontHave += "\nYou can not use ALL kinds of Path Cards UNLESS you repair all your tools"
            print(Tools_Have)
        print("------------------------------------------------------------------------------------")
        
        ligs,cols = Map.lenMap()
        c_map = Map.original()
        result = False
        
        #  ----------------------------------if he doesn't have all the tools------------------------------------
        if  (self.Light == False or self.Wagon == False or self.Pike == False):
            if (self.Light == False and self.Wagon == False ):
                i = 0
                for card in self.HandCards:
                    if (card[0] == Cards.ActionCards.LiW_DEF.value[0][0] and card[1] == Cards.ActionCards.LiW_DEF.value[0][1] and card[2] == Cards.ActionCards.LiW_DEF.value[0][2]) : 
                        CardChosed = card
                        self.Light = True
                        self.Wagon = True
                        Handcardschoice = i 
                        result = True
                        break
                    i += 1
            elif (self.Light == False and self.Pike == False):
                i = 0
                for card in self.HandCards:
                    if (card[0] == Cards.ActionCards.LiP_DEF.value[0][0] and card[1] == Cards.ActionCards.LiP_DEF.value[0][1] and card[2] == Cards.ActionCards.LiP_DEF.value[0][2]) :
                        CardChosed = card
                        self.Light = True
                        self.Pike = True
                        Handcardschoice = i 
                        result = True
                        break
                    i += 1
            elif (self.Pike == False and self.Wagon == False):
                i = 0
                for card in self.HandCards:
                    if (card[0] == Cards.ActionCards.PW_DEF.value[0][0] and card[1] == Cards.ActionCards.PW_DEF.value[0][1] and card[2] == Cards.ActionCards.PW_DEF.value[0][2]) :
                        CardChosed = card
                        self.Wagon = True
                        self.Pike = False
                        Handcardschoice = i 
                        result = True
                        break
                    i += 1
            elif (self.Light == False):
                i = 0
                for card in self.HandCards:
                    if (card[0] == Cards.ActionCards.Li_DEF.value[0][0] and card[1] == Cards.ActionCards.Li_DEF.value[0][1] and card[2] == Cards.ActionCards.Li_DEF.value[0][2]) :
                        CardChosed = card
                        self.Light = True
                        Handcardschoice = i 
                        result = True
                        break
                    i += 1
            elif (self.Pike == False):
                i = 0
                for card in self.HandCards:
                    if (card[0] == Cards.ActionCards.P_DEF.value[0][0] and card[1] == Cards.ActionCards.P_DEF.value[0][1] and card[2] == Cards.ActionCards.P_DEF.value[0][2]) :
                        CardChosed = card
                        self.Pike = True
                        Handcardschoice = i 
                        result = True
                        break
                    i += 1
            elif (self.Wagon == False):
                i = 0
                for card in self.HandCards:
                    if (card[0] == Cards.ActionCards.W_DEF.value[0][0] and card[1] == Cards.ActionCards.W_DEF.value[0][1] and card[2] == Cards.ActionCards.W_DEF.value[0][2]) :
                        CardChosed = card
                        self.Wagon = True
                        Handcardschoice = i 
                        result = True
                        break                       
                    i += 1
            
            if result == True :            
                print(f"card played is {CardChosed} : DEF CARD")
                return Handcardschoice
            
            else :          
                print("Card played : Pass his turn ")
                Handcardschoice = random.randint(1,len(self.HandCards)-1)
                print(f"he chosed to throw card {Handcardschoice + 1}")    
                return Handcardschoice
        
        #--------------------------------------the player has all the tools---------------------------------------
        else : 
            #-----------------------------------le joueur est un minier-----------------------------------------
            if self.identify == "Chercheur d'or" :
                
                # jouer une carte MAP 
                i = 0               
                for card in self.HandCards:
                    if card[0] == "( M )" and card[1] == "(MAP)" and card[2] == "( P )" and (self.map_use < 3) :
                        CardChosed = card
                        Handcardschoice = i
                        result = True
                            
                        if self.map_use == 0 : random.shuffle(self.tab_choice)
                        choice = self.tab_choice[self.map_use]
                        print(f"This terminal card {choice+1} is: ")
                        print(GoldPlace[choice][0])
                        print(GoldPlace[choice][1])
                        print(GoldPlace[choice][2])
                        self.map_use +=1
                        return Handcardschoice                        
                    i += 1
                    
                else :
                    # jouer une carte positive
                    i = 0
                    for card in self.HandCards:
                        for key,value in Cards.Path.Dic_Path.value.items():
                            if (value[0][0] == card[0]) and (value[0][1] == card[1]) and (value[0][2] == card[2]) and (value[1][0] == True) :
                                Handcardschoice = i
                                CardChosed = list(self.HandCards[Handcardschoice])
                                for x in range(ligs) :
                                    for y in range(cols-2) :
                                        result = Map.MapCurrentRobot(x,y,CardChosed,GoldPlace, 0)
                                        if result == False :
                                            result = Map.MapCurrentRobot(x,y,CardChosed,GoldPlace, 1)
                                        if result == True :
                                            self.x = x 
                                            self.y = y
                                            print(f"Card played : Path positive {Handcardschoice + 1} ")
                                            return Handcardschoice
                        i +=1
                        
                    # jouer une Rock Fall sur une carte négatif
                    i = 0
                    for card in self.HandCards:
                        if card[0] == "( R )" and card[1] == "(ROF)" and card[2] == "( F )"  :
                            x = 0
                            for ele in c_map :
                                y = 0
                                for val in ele :
                                    for key,value in Cards.Path.Dic_Path.value.items():
                                        if (value[0][0] == val[0]) and (value[0][1] == val[1]) and (value[0][2] == val[2]) and (value[1][0] == False) :
                                            Handcardschoice = i
                                            CardChosed = card
                                            result = Map.MapCurrentRobot(x,y,CardChosed,GoldPlace, 0)
                                            print(f"card played :{Handcardschoice + 1} : ROF  on {x},{y}")
                                            return Handcardschoice
                                    y = y + 1
                                x = x +1
                        i +=1
                     
                        
                    #throw card
                    
                    #throw path neg
                    i = 0
                    for card in self.HandCards :
                        for key,value in Cards.Path.Dic_Path.value.items():
                            if (value[0][0] == card[0]) and (value[0][1] == card[1]) and (value[0][2] == card[2]) and (value[1][0] == False) :
                                result = True 
                                Handcardschoice = i
                                print("Card played : Pass his turn ")
                                print(f"he chosed to throw card {Handcardschoice+1}")
                                return Handcardschoice
                        i = i+1
                        
                    #throw map card
                    i = 0
                    for card in self.HandCards :
                        if card[0] == "( M )" and card[1] == "(MAP)" and card[2] == "( P )" and (self.map_use >= 3) :
                            result = True 
                            Handcardschoice = i
                            print("Card played : Pass his turn ")
                            print(f"he chosed to throw card {Handcardschoice+1}")
                            return Handcardschoice
                        i = i+1

                    #throw ATT one tool
                    i = 0
                    for card in self.HandCards :
                        for key,value in Cards.ActionCards.Dic_OneTool.value.items():
                            if (value[0][0] == card[0]) and (value[0][1] == card[1]) and (value[0][2] == card[2]) and (value[1][0] == False) :
                                result = True 
                                Handcardschoice = i
                                print("Card played : Pass his turn ")
                                print(f"he chosed to throw card {Handcardschoice+1}")
                                return Handcardschoice
                        i = i+1

                    #throw ATT two tools
                    i = 0
                    for card in self.HandCards :
                        for key,value in Cards.ActionCards.Dic_TwoTools.value.items():
                            if (value[0][0] == card[0]) and (value[0][1] == card[1]) and (value[0][2] == card[2]) and (value[1][0] == False) :
                                result = True 
                                Handcardschoice = i
                                print("Card played : Pass his turn ")
                                print(f"he chosed to throw card {Handcardschoice+1}")
                                return Handcardschoice
                        i = i+1
 
                    #throw Rock Fall
                    i = 0
                    for card in self.HandCards :
                        if card[0] == "( R )" and card[1] == "(ROF)" and card[2] == "( F )"  :
                            result = True 
                            Handcardschoice = i
                            print("Card played : Pass his turn ")
                            print(f"he chosed to throw card {Handcardschoice+1}")
                            return Handcardschoice
                        i = i+1
                    
                    #random throw   
                    print("Card played : Pass his turn ")
                    Handcardschoice = random.randint(1,len(self.HandCards)-1)
                    print(f"he chosed to throw card {Handcardschoice}")    
                    return Handcardschoice
            
                #-----------------------------------le joueur est un SABOTEUR-----------------------------------------
            
            else :
                
                # jouer une carte MAP 
                i = 0               
                for card in self.HandCards:
                    if card[0] == "( M )" and card[1] == "(MAP)" and card[2] == "( P )" and (self.map_use < 3) :
                        CardChosed = card
                        Handcardschoice = i
                        result = True
                            
                        if self.map_use == 0 : random.shuffle(self.tab_choice)
                        choice = self.tab_choice[self.map_use]
                        print(f"This terminal card {choice+1} is: ")
                        print(GoldPlace[choice][0])
                        print(GoldPlace[choice][1])
                        print(GoldPlace[choice][2])
                        self.map_use +=1
                        return Handcardschoice                        
                    i += 1
                    
                else :
                    # jouer une carte negative
                    i = 0
                    for card in self.HandCards:
                        for key,value in Cards.Path.Dic_Path.value.items():
                            if (value[0][0] == card[0]) and (value[0][1] == card[1]) and (value[0][2] == card[2]) and (value[1][0] == False) :
                                Handcardschoice = i
                                CardChosed = list(self.HandCards[Handcardschoice])
                                for x in range(ligs) :
                                    for y in range(cols-2) :
                                        result = Map.MapCurrentRobot(x,y,CardChosed,GoldPlace, 0)
                                        if result == False :
                                            result = Map.MapCurrentRobot(x,y,CardChosed,GoldPlace, 1)
                                        if result == True :
                                            self.x = x 
                                            self.y = y
                                            print(f"Card played : Path negative {Handcardschoice + 1} ")
                                            return Handcardschoice
                        i +=1
                        
                    # jouer une Rock Fall sur une carte positif
                    i = 0
                    for card in self.HandCards:
                        if card[0] == "( R )" and card[1] == "(ROF)" and card[2] == "( F )"  :
                            x = 0
                            for ele in c_map :
                                y = 0
                                for val in ele :
                                    for key,value in Cards.Path.Dic_Path.value.items():
                                        if (value[0][0] == val[0]) and (value[0][1] == val[1]) and (value[0][2] == val[2]) and (value[1][0] == True) :
                                            Handcardschoice = i
                                            CardChosed = card
                                            result = Map.MapCurrentRobot(x,y,CardChosed,GoldPlace, 0)
                                            print(f"card played :{Handcardschoice + 1} : ROF  on {x},{y}")
                                            return Handcardschoice
                                    y = y + 1
                                x = x +1
                        i +=1
                        
                    #jouer une carte attaque
                    i = 0
                    for card in self.HandCards:
                        for key,value in Cards.ActionCards.Dic_OneTool.value.items():
                            if key == str(card):
                                target = random.randint(1, len(player-1))
                                while target != self.order :
                                    target = random.randint(1, len(player-1))
                                    target -= 1
                                if value[0] == 'Li' and player[target].Light != value[1]:
                                    player[target].Light = value[1]
                                    result = True
                                elif value[0] == 'P' and player[target].Pike != value[1]:
                                    player[target].Pike = value[1]
                                    result = True
                                elif value[0] == 'W' and player[target].Wagon != value[1]:
                                    player[target].Wagon = value[1]
                                    result = True                
                                if result == True:
                                    Handcardschoice = i
                                    CardChosed = card
                                    result = Map.MapCurrentRobot(x,y,CardChosed,GoldPlace, 0)
                                    print("card played :ATT")
                                return Handcardschoice
                        i = i+1
                        
                        
                    #throw card
                    
                    #throw path pos
                    i = 0
                    for card in self.HandCards :
                        for key,value in Cards.Path.Dic_Path.value.items():
                            if (value[0][0] == card[0]) and (value[0][1] == card[1]) and (value[0][2] == card[2]) and (value[1][0] == True) :
                                result = True 
                                Handcardschoice = i
                                print("Card played : Pass his turn ")
                                print(f"he chosed to throw card {Handcardschoice+1}")
                                return Handcardschoice
                        i = i+1
                        
                    #throw map card
                    i = 0
                    for card in self.HandCards :
                        if card[0] == "( M )" and card[1] == "(MAP)" and card[2] == "( P )" and (self.map_use >= 3) :
                            result = True 
                            Handcardschoice = i
                            print("Card played : Pass his turn ")
                            print(f"he chosed to throw card {Handcardschoice+1}")
                            return Handcardschoice
                        i = i+1

                    #throw DEF one tool
                    i = 0
                    for card in self.HandCards :
                        for key,value in Cards.ActionCards.Dic_OneTool.value.items():
                            if (value[0][0] == card[0]) and (value[0][1] == card[1]) and (value[0][2] == card[2]) and (value[1][0] == True) :
                                result = True 
                                Handcardschoice = i
                                print("Card played : Pass his turn ")
                                print(f"he chosed to throw card {Handcardschoice+1}")
                                return Handcardschoice
                        i = i+1

                    #throw DEF two tools
                    i = 0
                    for card in self.HandCards :
                        for key,value in Cards.ActionCards.Dic_TwoTools.value.items():
                            if (value[0][0] == card[0]) and (value[0][1] == card[1]) and (value[0][2] == card[2]) and (value[1][0] == True) :
                                result = True 
                                Handcardschoice = i
                                print("Card played : Pass his turn ")
                                print(f"he chosed to throw card {Handcardschoice+1}")
                                return Handcardschoice
                        i = i+1
                    
                    #random throw   
                    print("Card played : Pass his turn ")
                    Handcardschoice = random.randint(1,len(self.HandCards)-1)
                    print(f"he chosed to throw card {Handcardschoice}")    
                    return Handcardschoice
            
            
        return Handcardschoice
      



