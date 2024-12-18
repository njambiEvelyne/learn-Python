secret_guess = 7
gues_count = 0
guess_limit = 3

while gues_count < guess_limit:
    guess = int(input("Enter your guess: "))
    gues_count +=1
    if guess == secret_guess:
        print("You won!")
        break
else:
    print('Sorry, you failed!')
