import Random
number=range(1,50)
guess=input(input("Guess a number between 1 and 50: "))
while guess!=number:
    if guess< number:
        print("you've guessed too low,try again")
    guess=input(input("\n Guess a number between 1 and 50: "))
else:
    print("you've guessed too high,try again")
    guess=input(input("\n Guess a number between 1 and 50: "))
    print("you win!")
    
