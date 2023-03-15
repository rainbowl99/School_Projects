# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 15:34:03 2022

@author: 22044
"""


import random

class SabOOteur:
    def __init__(self):        
        pass

    def Welcome(self):
        info = ' Welcome to SabOOteurs, where dwarf otters look for gold in a mine! '
        print('+' + '-' * len(str(info)) + '+')
        print('|' + str(info) + '|')
        print('+' + '-' * len(str(info)) + '+')
    
    def Preparation(self,n):

        # Players
        PlayersOrder = []
        # # Human players
        HumanPlayers = []
        # # Robot Players 
        RobotPlayers = []
        # Status of all Players
        StatusPlayers = []
        print("-------------------------------------------------")
        res = f"The {n} players are: " 
        for i in range(n):
            name = input(f"Please enter the name of player {i+1} : ")
            status = ["IA","Human"]
            status_chosed = int(input(f"Please enter its status of player {i+1} (IA: 0, Human: 1): "))
            StatusPlayers.append(status_chosed)    
            
            while status_chosed != 0 and status_chosed != 1:
                print("The status should equal 0 or 1, please re-enter the status")
                status_chosed = int(input(f"Please enter its status of player {i+1} (IA: 0, Human: 1): "))
            
            res += f"\nPlayer {i+1}: {name}({status[status_chosed]})"
            
            PlayersOrder.append(f'{name}')
            
            if status_chosed == 0:
                RobotPlayers.append(f"{name}")
            elif status_chosed == 1:
                HumanPlayers.append(f"{name}")
        print("-------------------------------------------------")        
        print(res)
        return StatusPlayers,PlayersOrder
        
            
    # Shuffle the cards
    def ShuffleCards(self,cards):
        random.shuffle(cards)
    
    # Distribute 5 cards for every player
    def DistributeCards(self,deck,NumberHandCards):
        for i in range(self.n):
            HandCards = deck[:NumberHandCards]
            del deck[:NumberHandCards]
        return deck,HandCards
    
    def DistributeGold(self,Cards_Or,CheckWin,PlayersOrder,winner):
        num_Saboteur = 0
        
        for player in PlayersOrder:
            if player.identify == "Saboteur":
                num_Saboteur += 1
               
        
        random.shuffle(Cards_Or)
             
      
        winner_list = []
        
        #list of winner
        for player in PlayersOrder[winner.order:len(PlayersOrder)]:
            if player.identify == "Chercheur d'or":
                winner_list.append(player)
        for player in PlayersOrder[0:winner.order]:
            if player.identify == "Chercheur d'or":
                winner_list.append(player)

        if CheckWin == True: # Player find treasure
            Cards_Or_distribute = []
            if len(PlayersOrder) == 10: 
                for i in range (9):
                   Card_Or = Cards_Or.pop()
                   Cards_Or_distribute.append(Card_Or)
                Cards_Or_distribute.sort(reverse = True) 
                #distribute cards for winners
                persons = [[] for _ in range(len(winner_list))] 
                for i, card in enumerate(Cards_Or_distribute):
                    persons[i % len(winner_list)].append(card)   
                for i in range(len(winner_list)):
                    for j in persons[i]:
                        winner_list[i].gold += j
            else:   
                for i in range (len(PlayersOrder)):
                    Card_Or = Cards_Or.pop()
                    Cards_Or_distribute.append(Card_Or)
                Cards_Or_distribute.sort(reverse = True)
                #distribute cards for winners
                persons = [[] for _ in range(len(winner_list))]
                
                for i, card in enumerate(Cards_Or_distribute):
                    persons[i % len(winner_list)].append(card)               
                for i in range(len(winner_list)): 
                    for j in persons[i]:
                        winner_list[i].gold += j
                    
        
        if CheckWin != True: #Play do not find treasure
            if not any(player.identify == "Saboteur" for player in PlayersOrder): #There are not Saboteurs in the Player list
                pass
            a = Cards_Or.count(3)
            b = Cards_Or.count(2)
            c = Cards_Or.count(1)
            if num_Saboteur == 1 :                                            #There are Saboteurs in the Player list                                                           
                for player in PlayersOrder :
                    if player.identify == "Saboteur":
                        player.gold += 4
                        if a >= 1 and c >= 1 and len(Cards_Or) >= 2:
                            Cards_Or.remove(3)
                            Cards_Or.remove(1)
                        elif b >= 2 and a == 0 and len(Cards_Or) >= 2:
                            Cards_Or.remove(2)
                            Cards_Or.remove(2)
                        elif b == 1 and len(Cards_Or) >= 3:
                            Cards_Or.remove(2)
                            Cards_Or.remove(1)
                            Cards_Or.remove(1)
                        elif len(Cards_Or) >= 4:
                            Cards_Or.remove(1)
                            Cards_Or.remove(1)
                            Cards_Or.remove(1)
                            Cards_Or.remove(1)
            if num_Saboteur in [2,3]:
                for player in PlayersOrder :
                    if player.identify == "Saboteur":
                        player.gold += 3
                        if a >= 1 and len(Cards_Or) >= 1:
                            Cards_Or.remove(3)
                        elif a == 0 and b > 0 and len(Cards_Or) >= 2:
                            Cards_Or.remove(2)
                            Cards_Or.remove(1)
                        elif len(Cards_Or) >= 3:
                            Cards_Or.remove(1)
                            Cards_Or.remove(1)
                            Cards_Or.remove(1)
            if num_Saboteur == 4 :
                for player in PlayersOrder :
                    if player.identify == "Saboteur":
                        player.gold += 2
                        if b > 0 and len(Cards_Or) >= 1:
                            Cards_Or.remove(2)
                        elif len(Cards_Or) >= 2:
                            Cards_Or.remove(1)
                            Cards_Or.remove(1)
                            

        