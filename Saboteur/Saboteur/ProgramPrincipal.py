# -*- coding: utf-8 -*-
"""
Created on Fri Dec 23 14:21:50 2022

@author: 22044
"""
from SabOOteur import SabOOteur
from Cards import Cards
from Map import Map
from HumanPlayer import Human
from RobotPlayer import Robot

gamestart = SabOOteur()
cardstype = Cards()
MAP = Map()
# L'affichage de Welcome
gamestart.Welcome()


"""
Creat the deck

"""
# Deck of Action cards of Action cards:
Deck_Action = cardstype.ActionDeck()
# Deck of chemin cards of Path cards
Deck_chemin = cardstype.PathDeck() 
# Combine the two types of cards together.
Deck = list(Deck_Action) + list(Deck_chemin)
# Shuffule the deck
gamestart.ShuffleCards(Deck)


# Terminal Cards(GoldPlace)
GoldPlace = cardstype.TerminalType()
gamestart.ShuffleCards(GoldPlace)

print('round(1)')
"""
Create the identify cards

"""
# nb of players n and Identify cards
cardstype.Identify()
gamestart.ShuffleCards(cardstype.IdentifyCards)

# Order and type Players
StatusPlayers,PlayersOrders = gamestart.Preparation(cardstype.n)

i = 0
for player in StatusPlayers:
    if player == 0:
        PlayersOrders[i] = Robot(PlayersOrders[i], i, cardstype.IdentifyCards[i])
    else:
        PlayersOrders[i] = Human(PlayersOrders[i], i, cardstype.IdentifyCards[i])
    PlayersOrders[i].DistributeCards(Deck, cardstype.NumberHandCards)
    i += 1   

""" 
Start to play

"""
CardEmpty = [False]*cardstype.n
print(CardEmpty)
while MAP.ConditionOfWinning(GoldPlace) != True:
    
    i = 0    
    for player in PlayersOrders:
        
        i += 1 
        print("------------------------------------------------------------------------------------")
        if player.HandCards == []:
            CardEmpty[i-1] = True
        else:
            MAP.PrintMap()
            print(f"Player {i}, now it is your turn!")
            # Show player's HandCards
            player.PrintHandCards(player.HandCards)
            #Use a card(Incluing throwing away a card)
            CardChoice = player.Usecard(MAP,PlayersOrders,GoldPlace)
            player.DelCard(CardChoice)
            if Deck != []:
                player.GetCard(Deck)
            
        if MAP.ConditionOfWinning(GoldPlace) == True:
            MAP.PrintMap()
            break

    if all(CardEmpty) and MAP.ConditionOfWinning(GoldPlace) != True:        
        print('Saboteur Win!')
        break
    
CheckWin = MAP.ConditionOfWinning(GoldPlace)
Cards_Or = cardstype.Or()
winner = PlayersOrders[i-1]
gamestart.DistributeGold(Cards_Or,CheckWin,PlayersOrders,winner)

for order,player in enumerate(PlayersOrders):
    
    print(player.name,'has',end=' ')
    print(player.gold,'pépites')

rounds = 1
while rounds != 3:
    rounds += 1
    print('round',rounds)
    MAP.maporignal()
    print(MAP.map)
    """
    Creat the deck

    """

    # Deck of Action cards of Action cards:
    Deck_Action = cardstype.ActionDeck()
    # Deck of chemin cards of Path cards
    Deck_chemin = cardstype.PathDeck() 
    # Combine the two types of cards together.
    Deck = list(Deck_Action) + list(Deck_chemin)
    print(len(Deck))
    # Shuffule the deck
    gamestart.ShuffleCards(Deck)


    # Terminal Cards(GoldPlace)
    gamestart.ShuffleCards(GoldPlace)

    """
    Create the identify cards

    """

    gamestart.ShuffleCards(cardstype.IdentifyCards)


    i = 0
    for player in PlayersOrders:
        player.Initial(cardstype.IdentifyCards[i])
        PlayersOrders[i].DistributeCards(Deck, cardstype.NumberHandCards)
        i += 1   

    """ 
    Start to play

    """

    CardEmpty = [False]*cardstype.n
    print(CardEmpty)
    
    while MAP.ConditionOfWinning(GoldPlace) != True:
        
        i = 0    
        for player in PlayersOrders:
            
            i += 1 
            print("------------------------------------------------------------------------------------")
            if player.HandCards == []:
                CardEmpty[i-1] = True
            else:
                MAP.PrintMap()
                print(f"Player {i}, now it is your turn!")
                # Show player's HandCards
                player.PrintHandCards(player.HandCards)
                #Use a card(Incluing throwing away a card)
                CardChoice = player.Usecard(MAP,PlayersOrders,GoldPlace)
                player.DelCard(CardChoice)
                if Deck != []:
                    player.GetCard(Deck)
                
            if MAP.ConditionOfWinning(GoldPlace) == True:
                MAP.PrintMap()
                break

        if all(CardEmpty) and MAP.ConditionOfWinning(GoldPlace) != True:        
            print('Saboteur Win!')
            break
        
    CheckWin = MAP.ConditionOfWinning(GoldPlace)
    Cards_Or = cardstype.Or()
    winner = PlayersOrders[i-1]
    gamestart.DistributeGold(Cards_Or,CheckWin,PlayersOrders,winner)
    
    for order,player in enumerate(PlayersOrders):        
        print(player.name,'has',end=' ')
        print(player.gold,'pépites')


    




winner_list = []
for order,player in enumerate(PlayersOrders):
    
    print(player.name,'has',end=' ')
    print(player.gold,'pépites')

    if order >= 1:
        if PlayersOrders[order - 1].gold < player.gold:
            winner_list = []
            winner_list.append(player.name)
        elif PlayersOrders[order - 1].gold == player.gold:
            winner_list.append(player.name)
    elif order == 0:
        winner_list.append(player.name)
print('the winner is',winner_list)