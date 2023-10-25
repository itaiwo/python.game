import random

player_win = 0
computer_win = 0

while True:
    player = input("Enter your choice(rock, paper, scissor): ")
    game = ("rock", "paper", "scissor")
    computer = random.choice(game)
    
    print("player_choice: ", player)
    print("computer_choice: ", computer)
    

    if computer == player:
        print("It is a tie")
    elif computer == 'rock':
        if player ==  'scissor':
           print("You lose! Rock smashes scissor")
           computer_win += 1
        else:
            print("You win! Paper cover rock")
            player_win +=  1
    elif computer == 'paper':
        if player == 'rock':
            print("You lose! Paper cover rock")
            computer_win += 1
        else:
            print("You win! Scissor cut paper")
            player_win += 1
    elif computer == 'scissor':
        if player == 'paper':
            print("You lose! Scissor cut paper")
            computer_win += 1
        else:
            print("You win! Rock smashes scissor")
            player_win += 1
        
        
    print("You have " + str(player_win) + " wins")
    print("computer have " + str(computer_win) + " wins")                                            
                                            
          
              