from random import randint

def guess(x):
    num = randint(1, x)
    guess = 0
    while guess != num:
        guess = int(input(f"Guess a number between 1 and {x}: "))
        print(guess)
        if guess>num:
            print("Too high!")
        elif guess<num:
            print("Too low!")
    print(f"Great! You have found the number {num}!")       


def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback!='c':
        guess = randint(low,high)
        feedback = input(f"Is {guess} too high(H), too low(L), or correct(C)?").lower()
        if feedback == 'h':
            high = guess-1
        elif feedback == 'l':
            low = guess+1;
    print(f"Hurray! I have guessed the number {guess} correctly!")

computer_guess(100)
    