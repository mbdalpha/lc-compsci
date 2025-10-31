# Question 16(a)
# Examination Number:
from random import randint

def guess_game(max_guesses_allowed, difficulty):
    if difficulty == "H":
        secret_number = randint(1, 100)
    else:
        secret_number = randint(1, 5)
    guess_count = 0
    user_guess = 0
    g_list = []

    while (user_guess != secret_number and guess_count!=max_guesses_allowed):

        user_guess = int(input("Enter your guess: "))
        if user_guess in g_list:
            print("Ypu already guessed this number.")
        g_list.append(user_guess)
        guess_count += 1 #Increase guess_count by 1
        if user_guess == secret_number:
            print("Congratulations! You win!")
            print(f"You took {guess_count} guesses")
        elif user_guess > secret_number:
            print(f"Sorry! Your guess was too high")
        elif user_guess < secret_number:
            print(f"Sorry! Your guess was too low")

print("Welcome to the guessing game!")
max = int(input("Enter the maximum number of guesses allowed: "))
diff = input("Enter difficulty E(asy) or H(ard): ")
guess_game(max, diff)


# Question 16(b)
# Examination Number:

def game_round():
    user_score = 0
    play = True
    while play:
        computer_number = randint(1, 100) ##gets random number from 1 to 100 as the secret number
        user_number = int(input("Enter your guess: "))
        difference = abs(computer_number-user_number)
        print(f"Secret number is {computer_number}. You guessed {user_number}. Difference is {difference}.")
        if user_number == computer_number: ##checks if meets jackpot conditions
            user_score += 100
            print("JACKPOT!!! You score 100 points")
        elif difference < 21: ##if not jackpot, checks if within 20
            user_score +=20
            print("You score 20 points")
        elif difference > 30: ##if not jackpot, checks if beyond 30
            user_score -=30
            print("You lose 30 points")
        if input("Play again?(Y/N):") != "Y": ##when anything but 'Y' is inputted, game ends
            play = False

game_round()