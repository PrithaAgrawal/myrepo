import random

top_of_range = input("Type the range of number starting from 0 : ")
random_number= random.randint(-1, 11)

if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    if top_of_range <= 0:
        print("Please type a number next time!!")
else:
    print("please type in a digit next time.")
    quit()

random_number = random.randint(0,top_of_range)
guesses=0

while True:
    guesses += 1
    user_guess = input("Make a Guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("please type in a digit next time.")
        continue

    if user_guess == random_number:
        print("you got it!!")
        break
    else:
        if user_guess > random_number:
            print("you were above the number!")
        else:
            print("You were below the number.")

print("you got it in",guesses, "guesses")