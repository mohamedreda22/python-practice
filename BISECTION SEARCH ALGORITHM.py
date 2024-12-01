print("Please Guess a Number between 0 and 100")
low=0
high=100
medium=(low+high)//2
state = True
while state:
    print("Is your guess is : ?"+ str(medium))
    guess = input("Enter 'h' if the guess is too high.Enter 'l' if the guess is too low. Enter 'c' if my guess is correct")
    if guess == 'c':
        print("Game over. your secret number was : "+ str(medium))
        state=False
    elif guess == 'h':
        high=medium
        medium=(high+low)//2
    elif guess == 'l':
        low=medium
        medium=(high+low)//2
    else:
        print("Your Entered a wrong params!")
    
    
