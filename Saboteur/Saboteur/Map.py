# -*- coding: utf-8 -*-
"""
Created on Sun Dec 25 20:53:52 2022

@author: 22044
"""
from Cards import Cards

class Map:
    def __init__(self):
        # Creer la matrice vide de Map
        self.map =[[['     ']*3 for i in range(9)] for j in range(5)]
        
        # Placement des cartes de départ et d'arrivée.
        self.map[2][0] = Cards.Path.S.value[0]
        self.map[0][8] = Cards.Path.T1.value[0]
        self.map[2][8] = Cards.Path.T2.value[0]
        self.map[4][8] = Cards.Path.T3.value[0]
        
        
        # La premiere ligne d'affichage
        self.l0 = " |  " + "    ".join([f"{i}" for i in range(9)]) + "  "
        # La deuxieme ligne et la derniere ligne d'affichage
        self.l1 = self.ln = "-+"+"-"*9*5
        
        # Save all paths created
        self.AllPaths = []
        # 
        self.visited = [[2,0]]
        #
        self.X_end = [[0,8],[2,8],[4,8]]
        pass
    
     
    def original(self): 
         return self.map
    
    def lenMap(self):
        ligs = int(len(self.map))
        cols = int(len(self.map[0]))
        return ligs, cols
        
    def maporignal(self):
        maporiginal = [[['     ']*3 for i in range(9)] for j in range(5)]
        maporiginal[2][0] = Cards.Path.S.value[0]
        maporiginal[0][8] = Cards.Path.T1.value[0]
        maporiginal[2][8] = Cards.Path.T2.value[0]
        maporiginal[4][8] = Cards.Path.T3.value[0]
        self.map = maporiginal
        return
    
    def PrintMap(self):
        print("Current mine state")
        print(self.l0)
        print(self.l1)
        for i in range(len(self.map)):            
            res0 = res2 = " |"
            res1 = f"{i}|"
            for j in range(len(self.map[0])):
                # Concaténer les informations des cartes dans les positions correspondantes dans une chaîne(Position de la carte est[i,j]).
                res0 += self.map[i][j][0]
                res1 += self.map[i][j][1]
                res2 += self.map[i][j][2]
            print(res0)
            print(res1)
            print(res2)
        print(self.ln)
        return
    
    
    def MapCurrent(self,x,y,card,GoldPlace):
        map_LastTime = self.map
        ligs = int(len(self.map))
        cols = int(len(self.map[0]))
        # La position nouvelle de carte 
        x_n = x
        y_n = y
        
        if (x == ligs) or (x == -1):
            if (y <= -1) or (y >= cols):
                print("You can not place your card herr(Out of limitation),please re-enter the position")
                return False
            self.l0 = " |  " + "    ".join([f"{i}" for i in range(cols)]) + "  "
            self.l1 = self.ln = "-+"+"-"*cols*5
            if (x == ligs):
                self.map.append([['     ']*3 for i in range(cols)])
            else:
                x_n = 0
                self.map.insert(x_n, [['     ']*3 for i in range(cols)])
        elif (x >= 0) and (x < ligs):
            if (y == cols) or (y == -1):
                self.l0 = " |  " + "    ".join([f"{i}" for i in range(cols+1)]) + "  "
                self.l1 = self.ln = "-+"+"-"*(cols+1)*5
                if (y == cols):
                    for i in range(ligs):
                        self.map[i].append(['     ']*3)
                else:
                    y_n = 0
                    for i in range(ligs):
                        self.map[i].insert(y_n,['     ']*3)
            elif (y >= 0) and (y < cols):
                self.l0 = " |  " + "    ".join([f"{i}" for i in range(cols)]) + "  "
                self.l1 = self.ln = "-+"+"-"*(cols)*5
            else:
                print("You can not place your card here(Out of limitation),please re-enter the position")
                return False
                    
        else:
            print("You can not place your card here(Out of limitation),please re-enter the position")
            return False
        
            
        # Determine whether path cards and ROF cards can be placed on the map.
        if card == ["     ","     ","     "]: 
            judge = [element != "     " for element in self.map[x_n][y_n]]
            if (all(judge)) and (self.map[x_n][y_n] != Cards.Path.S.value[0]) and (self.map[x_n][y_n] != Cards.Path.T1.value[0]) and (self.map[x_n][y_n] != Cards.Path.T2.value[0]) and (self.map[x_n][y_n] != Cards.Path.T3.value[0]):
                self.map[x_n][y_n] = card
                return True
            else:
                print("No path card here. You can not place your card here,please re-enter the position")
                return False
        while card != ["     ","     ","     "]:
            judge = [element != "     " for element in self.map[x_n][y_n]]
            if all(judge):
                print("One path card here. You can not place your card here,please re-enter the position")
                return False
            else:

                DirectionOfCard = int(input("Which direction(Orignal State: 0; Rotate: 1.) of this card would you like to choose to place?"))
                if DirectionOfCard == 1:
                    cardrotate = []
                    cardrotate.append(card[2])
                    cardrotate.append(card[1][0] + card[1][3:0:-1] + card[1][4])
                    cardrotate.append(card[0])
                    card = cardrotate
                 
                # Place this card
                self.map[x_n][y_n] = card
                
                # The position of the card Start X_strat in the original coordinate system.
                X_end = []
                for i in range(int(len(self.map))):
                    for j, value in enumerate(self.map[i]):
                        if value == Cards.Path.S.value[0]:
                            X_start = [i,j]
                        elif value == Cards.Path.T1.value[0] or value == Cards.Path.T2.value[0]  or  value == Cards.Path.T3.value[0] or value == Cards.Path.Gold.value[0] or  value == Cards.Path.Rock.value[0]:
                            X_end.append([i,j])
                
                self.X_start = X_start
                self.X_end = X_end
                # Save all the queues(cards) on the map in an dictionnary Graph
                Graph = {}
                # For all positions on the map
                for j in range(len(self.map)):
                    for k,pos in enumerate(self.map[j]):
                        # When there is a card
                        card = self.map[j][k]
                        if pos != ["     ","     ","     "]:
                            # The new key(Position of this card) in dictionnary Graph created, and its value now is []
                            key_card = [j,k]
                            Graph[str(key_card)] = []
                            
                            # The positions of four directions of this card
                            CardsAround = [[j-1,k],
                                           [j,k+1],
                                           [j+1,k], 
                                           [j,k-1]]
                            # Diretion of this card: up:count = 1; right: count = 2; down: count = 3; left: count = 4
                            count = 0
                            # Justify if the routes of this card is connected to the cards around it, type of element in the list: Bool
                            if ([j,k] == end for end in X_end):
                                judgePath = [True]
                            else:
                                judgePath = []
                            
                            # If card_ii is a terminal card, then we check it is card Gold or Rock and we do not save its value in judgePath
                            cardsopen = [] 
                            # Start to justify the cards around
                            for card_i in CardsAround:
                                count += 1

                                # The around cards have their boundary and they need to exist(NOT EMPTY)
                                if card_i[0] >= 0 and card_i[1] >= 0 and card_i[0] < len(self.map) and card_i[1] < len(self.map[0]) and self.map[card_i[0]][card_i[1]] != ["     ","     ","     "]:
                                    # card_ii is the around card in the direction(count) of this card
                                    card_ii = self.map[card_i[0]][card_i[1]]
                                   
                                    if count == 1:
                                        card_X = [0,2]
                                        card_i_X =[2,2]
                                    elif count == 2:
                                        card_X = [1,3]
                                        card_i_X =[1,1]
                                    elif count == 3:
                                        card_X = [2,2]
                                        card_i_X =[0,2]
                                    elif count == 4:
                                        card_X = [1,1]
                                        card_i_X =[1,3]
                                    
                                    # When two is connected  
                                    if (card_ii != ['     ','     ','     '] and card_ii[card_i_X[0]][card_i_X[1]] != ' ' and card[card_X[0]][card_X[1]] != ' '):
                                        if card[card_X[0]][card_X[1]] == '|' or card[card_X[0]][card_X[1]] == '-':                                   
                                            
                                            for end in X_end:
                                                if card_i == end:
                                                    card_ii = Cards.Path.URDL_pos.value[0]

                                                    if self.map[card_i[0]][card_i[1]] == Cards.Path.T1.value[0]:
                                                        self.map[end[0]][end[1]] = GoldPlace[0]
                                                        terminalcheck = 0
                                                        print(0)
                                                        cardsopen.append(terminalcheck)
                                                    if self.map[card_i[0]][card_i[1]] == Cards.Path.T2.value[0]:
                                                        self.map[end[0]][end[1]] = GoldPlace[1]
                                                        terminalcheck = 1
                                                        print(1)
                                                        cardsopen.append(terminalcheck)
                                                        # cardsopen.append[1]
                                                    if self.map[card_i[0]][card_i[1]] == Cards.Path.T3.value[0]:
                                                        self.map[end[0]][end[1]] = GoldPlace[2]
                                                        terminalcheck = 2
                                                        print(2)
                                                        cardsopen.append(terminalcheck)

                                                    
                                        if card[card_X[0]][card_X[1]] == card_ii[card_i_X[0]][card_i_X[1]]:         
                                            for key,value in Cards.Path.Dic_Path.value.items(): 
                                                if value[0] == card_ii:
                                                    judgePath.append(value[1][0])
                                                    if value[1][0] == True:
                                                        # Append one noeud
                                                        Graph[str(key_card)].append(card_i)
                                        # When two is not connected
                                        elif card[card_X[0]][card_X[1]] == ' ' and card[card_X[0]][card_X[1]] != card_ii[card_i_X[0]][card_i_X[1]]:
                                            self.map = map_LastTime
                                            print("This path card does not connect the cards around it. You can not place your card here,please re-enter the position")
                                            return False
            
                            if judgePath == []:
                                self.map = map_LastTime
                                print("This path card does not have any cards around it. You can not place your card here,please re-enter the position")
                                return False
                

                def IsConnected(Graph,initial,X_start,visited = []):
                    visited.append(initial)
                    for neighbor in Graph[str(initial)]:   
                        if neighbor not in visited:
                            IsConnected(Graph, neighbor, X_start, visited)     
                    return visited
               
                        
                self.visited = IsConnected(Graph,[x_n,y_n] ,X_start) 
                

                if not any(f == X_start for f in self.visited):
                    self.map[x_n][y_n] = ['     ', '     ', '     ']
                    self.map = map_LastTime
                    print("You can not place your card here(IS Not Connected)")
                    return False
                
                


            break

        if cardsopen != []:
            for ele in cardsopen:
                if ele == 0:
                    self.map[X_end[0][0]][X_end[0][1]] = GoldPlace[0]
                elif ele == 1:
                    self.map[X_end[0][0]][X_end[0][1]] = GoldPlace[1]
                elif ele == 2:
                    self.map[X_end[0][0]][X_end[0][1]] = GoldPlace[2]
        return True
    
    def MapCurrentRobot(self,x,y,card,GoldPlace,DirectionOfCard):
        map_LastTime = self.map
        ligs = int(len(self.map))
        cols = int(len(self.map[0]))
        # La position nouvelle de carte 
        x_n = x
        y_n = y
        
        if (x == ligs) or (x == -1):
            if (y <= -1) or (y >= cols):
                return False
            self.l0 = " |  " + "    ".join([f"{i}" for i in range(cols)]) + "  "
            self.l1 = self.ln = "-+"+"-"*cols*5
            if (x == ligs):
                self.map.append([['     ']*3 for i in range(cols)])
            else:
                x_n = 0
                self.map.insert(x_n, [['     ']*3 for i in range(cols)])
        elif (x >= 0) and (x < ligs):
            if (y == cols) or (y == -1):
                self.l0 = " |  " + "    ".join([f"{i}" for i in range(cols+1)]) + "  "
                self.l1 = self.ln = "-+"+"-"*(cols+1)*5
                if (y == cols):
                    for i in range(ligs):
                        self.map[i].append(['     ']*3)
                else:
                    y_n = 0
                    for i in range(ligs):
                        self.map[i].insert(y_n,['     ']*3)
            elif (y >= 0) and (y < cols):
                self.l0 = " |  " + "    ".join([f"{i}" for i in range(cols)]) + "  "
                self.l1 = self.ln = "-+"+"-"*(cols)*5
            else:
                return False
                    
        else:
            return False
        
            
        # Determine whether path cards and ROF cards can be placed on the map.
        if card[0] == "( R )" and card[1] == "(ROF)"  and card[2] == "( F )" : 
            judge = [element != "     " for element in self.map[x_n][y_n]]
            if (all(judge)) and (self.map[x_n][y_n] != Cards.Path.S.value[0]) and (self.map[x_n][y_n] != Cards.Path.T1.value[0]) and (self.map[x_n][y_n] != Cards.Path.T2.value[0]) and (self.map[x_n][y_n] != Cards.Path.T3.value[0]):
                self.map[x_n][y_n] = ["     ","     ","     "]
                return True
            else:
                return False
        while card[0] != "( R )" and card[1] != "(ROF)"  and card[2] != "( F )" : 
            judge = [element != "     " for element in self.map[x_n][y_n]]
            if all(judge):
                return False
            else:

                if DirectionOfCard == 1:
                    cardrotate = []
                    cardrotate.append(card[2])
                    cardrotate.append(card[1][0] + card[1][3:0:-1] + card[1][4])
                    cardrotate.append(card[0])
                    card = cardrotate
                 
                # Place this card
                self.map[x_n][y_n] = card
                
                # The position of the card Start X_strat in the original coordinate system.
                X_end = []
                for i in range(int(len(self.map))):
                    for j, value in enumerate(self.map[i]):
                        if value == Cards.Path.S.value[0]:
                            X_start = [i,j]
                        elif value == Cards.Path.T1.value[0] or value == Cards.Path.T2.value[0]  or  value == Cards.Path.T3.value[0] or value == Cards.Path.Gold.value[0] or  value == Cards.Path.Rock.value[0]:
                            X_end.append([i,j])
                
                self.X_start = X_start
                self.X_end = X_end
                # Save all the queues(cards) on the map in an dictionnary Graph
                Graph = {}
                # For all positions on the map
                for j in range(len(self.map)):
                    for k,pos in enumerate(self.map[j]):
                        # When there is a card
                        card = self.map[j][k]
                        if pos != ["     ","     ","     "]:
                            # The new key(Position of this card) in dictionnary Graph created, and its value now is []
                            key_card = [j,k]
                            Graph[str(key_card)] = []
                            
                            # The positions of four directions of this card
                            CardsAround = [[j-1,k],
                                           [j,k+1],
                                           [j+1,k], 
                                           [j,k-1]]
                            # Diretion of this card: up:count = 1; right: count = 2; down: count = 3; left: count = 4
                            count = 0
                            # Justify if the routes of this card is connected to the cards around it, type of element in the list: Bool
                            if ([j,k] == end for end in X_end):
                                judgePath = [True]
                            else:
                                judgePath = []
                            
                            # If card_ii is a terminal card, then we check it is card Gold or Rock and we do not save its value in judgePath
                            cardsopen = [] 
                            # Start to justify the cards around
                            for card_i in CardsAround:
                                count += 1

                                # The around cards have their boundary and they need to exist(NOT EMPTY)
                                if card_i[0] >= 0 and card_i[1] >= 0 and card_i[0] < len(self.map) and card_i[1] < len(self.map[0]) and self.map[card_i[0]][card_i[1]] != ["     ","     ","     "]:
                                    # card_ii is the around card in the direction(count) of this card
                                    card_ii = self.map[card_i[0]][card_i[1]]
                                   
                                    if count == 1:
                                        card_X = [0,2]
                                        card_i_X =[2,2]
                                    elif count == 2:
                                        card_X = [1,3]
                                        card_i_X =[1,1]
                                    elif count == 3:
                                        card_X = [2,2]
                                        card_i_X =[0,2]
                                    elif count == 4:
                                        card_X = [1,1]
                                        card_i_X =[1,3]
                                    
                                    # When two is connected  
                                    if (card_ii != ['     ','     ','     '] and card_ii[card_i_X[0]][card_i_X[1]] != ' ' and card[card_X[0]][card_X[1]] != ' '):
                                        if card[card_X[0]][card_X[1]] == '|' or card[card_X[0]][card_X[1]] == '-':                                   
                                            
                                            for end in X_end:
                                                if card_i == end:
                                                    card_ii = Cards.Path.URDL_pos.value[0]

                                                    if self.map[card_i[0]][card_i[1]] == Cards.Path.T1.value[0]:
                                                        self.map[end[0]][end[1]] = GoldPlace[0]
                                                        terminalcheck = 0
                                                        print(0)
                                                        cardsopen.append(terminalcheck)
                                                    if self.map[card_i[0]][card_i[1]] == Cards.Path.T2.value[0]:
                                                        self.map[end[0]][end[1]] = GoldPlace[1]
                                                        terminalcheck = 1
                                                        print(1)
                                                        cardsopen.append(terminalcheck)
                                                        # cardsopen.append[1]
                                                    if self.map[card_i[0]][card_i[1]] == Cards.Path.T3.value[0]:
                                                        self.map[end[0]][end[1]] = GoldPlace[2]
                                                        terminalcheck = 2
                                                        print(2)
                                                        cardsopen.append(terminalcheck)

                                                    
                                        if card[card_X[0]][card_X[1]] == card_ii[card_i_X[0]][card_i_X[1]]:         
                                            for key,value in Cards.Path.Dic_Path.value.items(): 
                                                if value[0] == card_ii:
                                                    judgePath.append(value[1][0])
                                                    if value[1][0] == True:
                                                        # Append one noeud
                                                        Graph[str(key_card)].append(card_i)
                                        # When two is not connected
                                        elif card[card_X[0]][card_X[1]] == ' ' and card[card_X[0]][card_X[1]] != card_ii[card_i_X[0]][card_i_X[1]]:
                                            self.map = map_LastTime
                                            return False
            
                            if judgePath == []:
                                self.map = map_LastTime
                                return False
                

                def IsConnectedR(Graph,initial,X_start,visited = []):
                    visited.append(initial)
                    for neighbor in Graph[str(initial)]:   
                        if neighbor not in visited:
                            IsConnectedR(Graph, neighbor, X_start, visited)     
                    return visited
               
                        
                self.visited = IsConnectedR(Graph,[x_n,y_n] ,X_start) 
                

                if not any(f == X_start for f in self.visited):
                    self.map[x_n][y_n] = ['     ', '     ', '     ']
                    self.map = map_LastTime
                    return False
                
                


            break

        if cardsopen != []:
            for ele in cardsopen:
                if ele == 0:
                    self.map[X_end[0][0]][X_end[0][1]] = GoldPlace[0]
                elif ele == 1:
                    self.map[X_end[0][0]][X_end[0][1]] = GoldPlace[1]
                elif ele == 2:
                    self.map[X_end[0][0]][X_end[0][1]] = GoldPlace[2]
        return True 
    
    def ConditionOfWinning(self,GoldPlace):
        for Xend in self.X_end:
            if self.map[Xend[0]][Xend[1]] == Cards.Path.Gold.value[0]:
                print('Chercheur or win! Game is Over! ')
                return True

            