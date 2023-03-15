# -*- coding: utf-8 -*-
"""
Created on Sun Dec 25 14:35:02 2022

@author: 22044
"""

from Player import Player
from Cards import Cards

class Human(Player):
    def __init__(self,name,order,identify):
        super().__init__(name,order,identify)
        
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
        
        result = False
        while result == False:
            # Choose what card to play
            Handcardschoice = int(input("What card would you like to play? "))
            while Handcardschoice < 1 or Handcardschoice > len(self.HandCards)+1:
                Handcardschoice = int(input(f"You can only select integers from 1 to {len(self.HandCards)+1}. Please choose the card you would like to play: "))

            # Throw away a card
            if Handcardschoice == len(self.HandCards)+1:
                Throwcardchoice = int(input("What card would you like to throw away? "))
                while Throwcardchoice < 1 or Throwcardchoice > len(self.HandCards):
                    Throwcardchoice = int(input(f"You can only select integers from 1 to {len(self.HandCards)}. Please choose the card you would like to throw away: "))
                Handcardschoice = Throwcardchoice-1
                return Handcardschoice
                
            
            Handcardschoice -= 1
            CardChosed = list(self.HandCards[Handcardschoice])
            # Use the card chosed        
            # Determine whether the current player's tools are complete.
            if (self.Light == False or self.Pike == False or self.Wagon == False):
                for key,value in Cards.Path.Dic_Path.value.items(): 
                    if value[0] == CardChosed:
                        print(Tools_DontHave)
                        break
                       
            else:
                for key,value in Cards.Path.Dic_Path.value.items(): 
                    if (value[0] == CardChosed) and (value[1]):
                        while True:
                            try:
                                self.x = int(input("Where do you want to place your card (x)? "))
                                break
                            except ValueError:
                                print('Invalid input. Please try again.')
                        
                        while True:
                            try:
                                self.y = int(input("Where do you want to place your card (y)? "))
                                break
                            except ValueError:
                                print('Invalid input. Please try again.')

                        result = Map.MapCurrent(self.x,self.y,CardChosed,GoldPlace)       
                        break
                        # del self.HandCards[Handcardschoice]

        
            
            # Use an Action Card
            for key,value in Cards.ActionCards.Dic_OneTool.value.items():
                if key == str(CardChosed):
                    target = int(input("Who is your tool card aimed at? "))
                    while target < 1 or target > len(player):
                        target = int(input("we do not have the information of this player, please re-choose your target "))
                    target -= 1
                    # for key,value in Cards.ActionCards.Dic_OneTool.value:
                    #     if  key == str(CardChosed):
                    if value[0] == 'Li' and player[target].Light != value[1]:
                        player[target].Light = value[1]
                        result = True
                    elif value[0] == 'P' and player[target].Pike != value[1]:
                        player[target].Pike = value[1]
                        result = True
                    elif value[0] == 'W' and player[target].Wagon != value[1]:
                        player[target].Wagon = value[1]
                        result = True
                    else:
                        print("Your target player has already (lost) the tool. Please re-choose your card. ")
                    
            for key,value in Cards.ActionCards.Dic_TwoTools.value.items():
                if key == str(CardChosed):
                    target = int(input("Who is your tool card aimed at? "))
                    while target < 1 or target > len(player):
                        target = int(input("we do not have the information of this player, please re-choose your target "))
                        
                    target -= 1
                    
                    # for key,value in Cards.ActionCards.Dic_OneTool.value:
                    #     if  key == str(CardChosed):
                    ToolNumber = int(input(f"Which tool({value[0][0]}:0,{value[1][0]}:1) would you like to use? "))
                    if value[ToolNumber][0] == 'Li' and player[target].Light != value[ToolNumber][1]:
                        player[target].Light = value[ToolNumber][1]
                        result = True
                    elif value[ToolNumber][0] == 'P' and player[target].Pike != value[ToolNumber][1]:
                        player[target].Pike = value[ToolNumber][1]
                        result = True
                    elif value[ToolNumber][0] == 'W' and player[target].Wagon != value[ToolNumber][1]:
                        player[target].wagon = value[ToolNumber][1]
                        result = True
                    else:
                        print("Your target player already has (lost) the tool. Please re-choose your card. ")
                    
            for key,value in Cards.ActionCards.Dic_Map.value.items():
                if key == str(CardChosed):
                    choice = int(input("Which Terminal Card(Up: 1; Middle: 2; Down: 3.) would like to check? "))
                    while choice < 1 or choice > 3:
                        choice = int(input("You only can enter the number 1 or 2 or 3). Which Terminal Card would like to check? "))
                    choice -= 1
                    print("This terminal card is: ")
                    print(GoldPlace[choice][0])
                    print(GoldPlace[choice][1])
                    print(GoldPlace[choice][2])
                    result = True
                    
            for key,value in Cards.ActionCards.Dic_ROF.value.items():
                if key == str(CardChosed):
                    while True:
                        try:
                            self.x = int(input("Where do you want to place your card (x)? "))
                            break
                        except ValueError:
                            print('Invalid input. Please try again.')
                    
                    while True:
                        try:
                            self.y = int(input("Where do you want to place your card (y)? "))
                            break
                        except ValueError:
                            print('Invalid input. Please try again.')
                    result = Map.MapCurrent(self.x,self.y,CardChosed,GoldPlace)
                    #Cards.ActionCards.Dic_ROF.value[str(CardChosed)]
        return Handcardschoice