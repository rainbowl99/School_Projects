# -*- coding: utf-8 -*-
"""
Created on Sun Dec 25 20:51:04 2022

@author: 22044
"""
import numpy as np
import enum

class Cards:
    class Path(enum.Enum):
        URDL_pos = [["( | )", "(-+-)", "( | )"]]
        URDL_pos_jug = [[True,True,True,True,True]]
        URDL_neg = [["( | )", "(-x-)", "( | )"]]
        URDL_neg_jug = [[False,True,True,True,True]]

        URD_pos = [["( | )", "( +-)", "( | )"]]
        URD_pos_jug = [[True,True,True,True,False]]
        URD_neg = [["( | )", "( x-)", "( | )"]]
        URD_neg_jug = [[False,True,True,True,False]]
    
        URL_pos = [["( | )", "(-+-)", "(   )"]]
        URL_pos_jug = [[True,True,True,False,True]]
        URL_neg = [["( | )", "(-x-)", "(   )"]]
        URL_neg_jug = [[False,True,True,False,True]]
    
        UR_pos = [["( | )", "( +-)", "(   )"]]
        UR_pos_jug = [[True,True,True,False,False]]
        UR_neg = [["( | )", "( x-)", "(   )"]]
        UR_neg_jug = [[False,True,True,False,False]]
    
        UL_pos = [["( | )", "(-+ )", "(   )"]]
        UL_pos_jug = [[True,True,False,False,True]]
        UL_neg = [["( | )", "(-x )", "(   )"]]
        UL_neg_jug = [[False,True,False,False,True]]
    
        UD_pos = [["( | )", "( + )", "( | )"]]
        UD_pos_jug = [[True,True,False,True,False]]
        UD_neg = [["( | )", "( x )", "( | )"]]
        UD_neg_jug = [[False,True,False,True,False]]
        
        RL_pos = [["(   )", "(-+-)", "(   )"]]
        RL_pos_jug = [[True,False,True,False,True]]
        RL_neg = [["(   )", "(-x-)", "(   )"]]
        RL_neg_jug = [[False,False,True,False,True]]
    
        U = [["( | )", "( x )", "(   )"]]
        U_jug = [[False,True,False,False,False]]
        R = [["(   )", "( x-)", "(   )"]]
        R_jug = [[False,False,True,False,False]]
        

        URD_pos1 = [["( | )", "(-+ )", "( | )"]]
        URD_pos_jug1 = [[True,True,False,True,True]]
        URD_neg1 = [["( | )", "(-x )", "( | )"]]
        URD_neg_jug1 = [[False,True,False,True,True]]
    
        URL_pos1 = [["(   )", "(-+-)", "( | )"]]
        URL_pos_jug1 = [[True,False,True,True,True]]
        URL_neg1 = [["(   )", "(-x-)", "( | )"]]
        URL_neg_jug1 = [[False,False,True,True,True]]
    
        UR_pos1 = [["(   )", "(-+ )", "( | )"]]
        UR_pos_jug1 = [[True,False,False,True,True]]
        UR_neg1 = [["(   )", "(-x )", "( | )"]]
        UR_neg_jug1 = [[False,False,False,True,True]]
    
        UL_pos1 = [["(   )", "( +-)", "( | )"]]
        UL_pos_jug1 = [[True,False,True,True,False]]
        UL_neg1 = [["(   )", "( x-)", "( | )"]]
        UL_neg_jug1 = [[False,False,True,True,False]]
    
        U1 = [["(   )", "( x )", "( | )"]]
        U_jug1 = [[False,False,False,True,False]]
        R1 = [["(   )", "(-x )", "(   )"]]
        R_jug1 = [[False,False,False,False,True]]
        
        
        S = [["( | )", "(-S-)", "( | )"]]
        S_jug = [[True,True,True,True,True]]
        T1 = [["( 1 )", "(END)", "( 1 )"]] 
        T2 = [["( 2 )", "(END)", "( 2 )"]] 
        T3 = [["( 3 )", "(END)", "( 3 )"]] 
        
        Gold = [["( | )", "(-G-)", "( | )"]]
        Gold_jug = [[True,True,True,True,True]]
        Rock = [["( | )", "(-R-)", "( | )"]]
        Rock_jug = [[False,True,True,True,True]]
        # Path Cards Dictionary
        Dic_Path =  {"URDL_pos":URDL_pos + URDL_pos_jug,
                    "URDL_neg": URDL_neg + URDL_neg_jug,
                    "URD_pos": URD_pos + URD_pos_jug,
                    "URD_neg": URD_neg + URD_neg_jug,
                    "URL_pos": URL_pos + URL_pos_jug,
                    "URL_neg": URL_neg + URL_neg_jug,
                    "UR_pos": UR_pos + UR_pos_jug,
                    "UR_neg": UR_neg + UR_neg_jug,
                    "UL_pos": UL_pos + UL_pos_jug,
                    "UL_neg": UL_neg + UL_neg_jug,
                    "UD_pos": UD_pos + UD_pos_jug,
                    "UD_neg": UD_neg + UD_neg_jug,
                    "RL_pos": RL_pos + RL_pos_jug,
                    "RL_neg": RL_neg + RL_neg_jug,
                    "U": U + U_jug,
                    "R": R + R_jug,
                    "URD_pos1": URD_pos1 + URD_pos_jug1,
                    "URD_neg1": URD_neg1 + URD_neg_jug1,
                    "URL_pos1": URL_pos1 + URL_pos_jug1,
                    "URL_neg1": URL_neg1 + URL_neg_jug1,
                    "UR_pos1": UR_pos1 + UR_pos_jug1,
                    "UR_neg1": UR_neg1 + UR_neg_jug1,
                    "UL_pos1": UL_pos1 + UL_pos_jug1,
                    "UL_neg1": UL_neg1 + UL_neg_jug1,
                    "U1": U1 + U_jug1,
                    "R1": R1 + R_jug1,
                    "S": S + S_jug,
                    "Gold": Gold + Gold_jug,
                    "Rock": Rock + Rock_jug}
    class ActionCards(enum.Enum):
        Li_ATT = [["(ATT)","( L )","(   )"]]
        Li_DEF = [["(DEF)","( L )","(   )"]]
        P_ATT = [["(ATT)","( P )","(   )"]]
        P_DEF = [["(DEF)","( P )","(   )"]]
        W_ATT = [["(ATT)","( W )","(   )"]]
        W_DEF = [["(DEF)","( W )","(   )"]]
        LiP_DEF = [["(DEF)","( L )","( P )"]]
        LiW_DEF = [["(DEF)","( L )","( W )"]]
        PW_DEF = [["(DEF)","( P )","( W )"]]
        MAP_EXPLORATION = [["( M )","(MAP)","( P )"]]
        ROF = [["( R )","(ROF)","( F )"]]
        
        
        # Action Cards Dictionary

        Dic_Map = {f"{MAP_EXPLORATION[0]}":["MAP"]}
        Dic_ROF = {f"{ROF[0]}":["     ","     ","     "]}
        Dic_OneTool = {f"{Li_ATT[0]}":["Li",False],
                        f"{Li_DEF[0]}":["Li",True],
                        f"{P_ATT[0]}":["P",False],
                        f"{P_DEF[0]}":["P",True],
                        f"{W_ATT[0]}":["W",False],
                        f"{W_DEF[0]}":["W",True]}
        
        Dic_TwoTools = {f"{LiP_DEF[0]}":[["Li",True],["P",True]],
                        f"{LiW_DEF[0]}":[["Li",True],["W",True]],
                        f"{PW_DEF[0]}":[["P",True],["W",True]]}
        

        
    def __init__(self):       
        
        # Path Cards Deck
        self.Path = np.vstack((Cards.Path.URDL_pos.value*5,Cards.Path.URDL_neg.value,
                                 Cards.Path.URD_pos.value*5,Cards.Path.URD_neg.value,
                                 Cards.Path.URL_pos.value*5,Cards.Path.URL_neg.value,
                                 Cards.Path.UR_pos.value*5,Cards.Path.UR_neg.value,
                                 Cards.Path.UL_pos.value*4,Cards.Path.UL_neg.value,
                                 Cards.Path.UD_pos.value*4,Cards.Path.UD_neg.value,
                                 Cards.Path.RL_pos.value*3,Cards.Path.RL_neg.value,
                                 Cards.Path.U.value,Cards.Path.R.value))
        # self.Path = np.vstack(Cards.Path.URDL_pos.value*100)

                             
        # Action Cards Deck
        self.action = np.vstack((Cards.ActionCards.Li_ATT.value*3,Cards.ActionCards.Li_DEF.value*2,
                                  Cards.ActionCards.P_ATT.value*3,Cards.ActionCards.P_DEF.value*2,
                                  Cards.ActionCards.W_ATT.value*3,Cards.ActionCards.W_DEF.value*2,
                                  Cards.ActionCards.LiP_DEF.value,
                                  Cards.ActionCards.LiW_DEF.value,
                                  Cards.ActionCards.PW_DEF.value,
                                  Cards.ActionCards.PW_DEF.value,
                                  Cards.ActionCards.MAP_EXPLORATION.value*6,
                                  Cards.ActionCards.ROF.value*3))
        
        # Starting Point
        self.S = Cards.Path.S.value[0]
        # Terminal point
        self.T1 = Cards.Path.T1.value[0]
        self.T2 = Cards.Path.T2.value[0]
        self.T3 = Cards.Path.T3.value[0]
        
        self.Gold = Cards.Path.Gold.value
        
        self.Rock = Cards.Path.Rock.value
        
        self.NumberHandCards = 0
        self.n = 0
        
    def Or(self):
        Cards_Or = [1]*16 + [2]*8 + [3]*4
        return Cards_Or

    def PathDeck(self):
        # Path Cards Deck
        return self.Path

    def ActionDeck(self):
        # Action Cards Deck
        return self.action             

    
    def Identify(self):
        self.n = int(input("How many players? "))
        while self.n > 10 or self.n < 3:
            print("You cannot start the game with the current number of players, please modify the number of players.")
            self.n = int(input ("Please re-enter the number of players : "))
                  
        if self.n == 3:
            self.IdentifyCards = ["Chercheur d'or"]*3+["Saboteur"]*1
            self.NumberHandCards = 6
        elif self.n == 4:
            self.IdentifyCards = ["Chercheur d'or"]*4+["Saboteur"]*1
            self.NumberHandCards = 6
        elif self.n == 5:
            self.IdentifyCards = ["Chercheur d'or"]*4+["Saboteur"]*2
            self.NumberHandCards = 6
        elif self.n == 6:
            self.IdentifyCards = ["Chercheur d'or"]*5+["Saboteur"]*2
            self.NumberHandCards = 5
        elif self.n == 7:
            self.IdentifyCards = ["Chercheur d'or"]*5+["Saboteur"]*3
            self.NumberHandCards = 5
        elif self.n == 8:
            self.IdentifyCards = ["Chercheur d'or"]*6+["Saboteur"]*3
            self.NumberHandCards = 4
        elif self.n == 9:
            self.IdentifyCards = ["Chercheur d'or"]*7+["Saboteur"]*3
            self.NumberHandCards = 4
        elif self.n == 10:
            self.IdentifyCards = ["Chercheur d'or"]*7+["Saboteur"]*4
            self.NumberHandCards = 4
            

        
        return 
    
    def Start(self):
        return self.S
    
    def Terminal(self):
        return self.T
    
    def TerminalType(self):
        Terminal_Status = self.Gold + self.Rock*2
        return Terminal_Status