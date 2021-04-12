from random import randint as r

def guess(x, y, lives):
    num = r(x, y)
    upper, lower = y, x
    c=0
    while True:
        n = int(input("\nGuess the number: "))
        
        if num == n:
            c=c+1
            print(f"Congratulations, you guessed the correct number in {c} guesses!!")
            break
        elif n < x or n > y:
            print(f"Number should be within the range {x}-{y}.")
        else:
            c=c+1
            lives=lives-1
            if lives == 0:
                print(f"Sorry, but the correct number was {num}.")
                break
            if n < num:
                lower = n
                level = "low"
            elif n > num:
                upper = n
                level = "high"
            print(f"You guessed the wrong number. Lives:{lives}.")
            print(f"Your guess is too {level}.")


print("-"*45)
print("    Welcome to the Number Guessing Game!!    ")
print("-"*45)
print("\nThere are 3 levels of the game.")
print("Press the given number to enter the corresponding level.")
print(" -Easy (Range between 1-10,3 lives)      (1)")
print(" -Medium (Range between 1-100,10 lives)  (2)")
print(" -Hard (Range between 1-1000,20 lives)   (3)")

while True:
    ch = int(input("\nEnter your choice: "))
    if ch == 1:
        guess(1, 10, 3)
        break
    elif ch == 2:
        guess(1, 100, 10)
        break
    elif ch == 3:
        guess(1, 1000, 20)
        break
    else:
        print("Invalid Choice. Please Try Again.\n")
        continue

print("Thanks for playing!!")

