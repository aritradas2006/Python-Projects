from random import choice 
print("-"*50)
print("    Welcome to the Rock,Paper and Scissors Game!!    ")
print("-"*50)
print("\nThere are 2 modes of the game.")
print("Press the given number to enter the corresponding mode.")
print(" -Player vs Computer (1)")
print(" -Player vs Player   (2)")

c=["rock","paper","scissors"]
while True:
    ch=int(input("\nWhich mode do you want to play in? "))
    if ch==1:
        computer_move=choice(c)
        while True:
            player_move=int(input("\nEnter 1 for rock,2 for paper and 3 for scissors: "))
            if player_move==1:
                if computer_move=="paper":
                    print("You're defeated as I chose paper!!")
                elif computer_move=="scissors":
                    print("You win as I chose scissors!!")
                else:
                    print("It's a tie as we both chose rock!!")
                
            elif player_move==2:
                if computer_move=="scissors":
                    print("You're defeated as I chose scissors!!")
                elif computer_move=="rock":
                    print("You win as I chose rock!!")
                else:
                    print("It's a tie as we both chose scissors!!")
                
            elif player_move==3:
                if computer_move=="rock":
                    print("You're defeated as I chose rock!!")
                elif computer_move=="paper":
                    print("You win as I chose paper!!")
                else:
                    print("It's a tie as we both chose scissors!!")
            else:
                print("Invalid Input.Please Try Again.")
                continue
            break
    else:
        print("Invalid Input.Please Try Again.")
        continue
    break
print("Thanks for playing!!")