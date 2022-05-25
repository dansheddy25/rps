move1 = ["R", "S"] 
move2 = ["S", "P"] 
move3 = ["P", "R"] 
player1 = [] 
player2 = [] 
draw = 0 
win_player1 = 0 
win_player2 = 0 
ranges_score = 0 
    
with open("player1.txt", "r") as file: 
    for moves in file: 
        moves = moves.strip() 
        player1.append(moves) 
        
with open("player2.txt", "r") as file: 
    for moves in file: 
        moves = moves.strip() 
        player2.append(moves) 
        ranges_score = len(player2) 

for i in range(ranges_score): 
    if player1[i] == player2[i]: 
        draw += 1

    elif ((player1[i] == 'R') & (player2[i] == 'S')) |((player1[i] == 'S') & (player2[i] == 'P')) | ((player1[i] == 'P') & (player2[i] == 'R')) :
        win_player1 += 1
    elif ((player2[i] == 'R') & (player1[i] == 'S')) | ((player2[i] == 'S') & (player1[i] == 'P')) | ((player2[i] == 'P') & (player1[i] == 'R')) :
        win_player2 += 1
            
count_player1 = str(win_player1)
count_player2 = str(win_player2)
count_draw = str(draw)
                                                            
with open("result.txt", "w") as file: 
    file.write("Player1 wins: " +  count_player1 + "\n") 
    file.write("Player2 wins: " +  count_player2 + "\n") 
    file.write("Draws: " + count_draw + "\n") 
    
    
print("Player1 wins: ", count_player1) 
print("Player2 wins: ", count_player2) 
print("Draws: ", count_draw)


#The correct output for Player1 wins:  31, Player2 wins:  26 and Draws:  43

