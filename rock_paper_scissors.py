# Make a rock paper scissors app that I can play against the computer. 
# The program should keep track of the number of rounds played, the number of rounds
# won by the user, and the number of rounds won by the computer. 
# After each round, the program should display the results 
# and ask the user if they want to play another round. 
# You should use functions, loops, conditionals, random number generation to achieve this.
import random

rounds=0
user_win=0
computer_win=0
drawn=0
while True:
    print("""
    Rock Paper Scissors  
    \n Please choose an option below 
    \n 1. Rock
    \n 2. Paper 
    \n 3. Scissors
    """)

    choise = (input("Enter an option: ")).lower()
    computer_choise = random.randint(1,3)
    if choise == "1" or choise =="rock":
        if computer_choise == 1:
            print("You chose Rock, and the computer chose Rock - You have drawn!")
            drawn += 1
            print(f"You have won {user_win} rounds and the computer has won {computer_win} rounds and there has been {drawn} rounds drawn \n========================================================================================")
        elif computer_choise == 2:
            print("You chose Rock, but the computer chose Paper - You lost!")
            computer_win+= 1
            print(f"You have won {user_win} rounds and the computer has won {computer_win} rounds and there has been {drawn} rounds drawn \n========================================================================================")
        elif computer_choise == 3:
            print("You chose Rock, but the computer chose Scissors - You win!")
            user_win += 1
            print(f"You have won {user_win} rounds and the computer has won {computer_win} rounds and there has been {drawn} rounds drawn \n========================================================================================")
    elif choise == "2" or choise =="paper":
        if computer_choise == 1:
            print("You chose Paper, and the computer chose Rock - You won!")
            user_win += 1
            print(f"You have won {user_win} rounds and the computer has won {computer_win} rounds and there has been {drawn} rounds drawn \n========================================================================================")
        elif computer_choise == 2:
            print("You chose Paper, but the computer chose Paper - You have drawn!")
            drawn+= 1
            print(f"You have won {user_win} rounds and the computer has won {computer_win} rounds and there has been {drawn} rounds drawn \n========================================================================================")
        elif computer_choise == 3:
            print("You chose Paper, but the computer chose Scissors - You lost!")
            computer_win += 1
            print(f"You have won {user_win} rounds and the computer has won {computer_win} rounds and there has been {drawn} rounds drawn \n========================================================================================")
    elif choise == "3" or choise =="scissors":
        if computer_choise == 1:
            print("You chose Scissors, and the computer chose Rock - You lost!")
            computer_win += 1
            print(f"You have won {user_win} rounds and the computer has won {computer_win} rounds and there has been {drawn} rounds drawn \n========================================================================================")
        elif computer_choise == 2:
            print("You chose Scissors, but the computer chose Paper - You win!")
            user_win+= 1
            print(f"You have won {user_win} rounds and the computer has won {computer_win} rounds and there has been {drawn} rounds drawn \n========================================================================================")
        elif computer_choise == 3:
            print("You chose Scissors, but the computer chose Scissors - You have drawn!")
            drawn += 1
            print(f"You have won {user_win} rounds and the computer has won {computer_win} rounds and there has been {drawn} rounds drawn \n========================================================================================")
    else:
        print("You have inputted an invalid choise, please re-enter either the name of the action (e.g. Rock) or the number (e.g. 1)")
    
        


