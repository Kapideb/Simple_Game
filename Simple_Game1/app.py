
import random
import time


def game():
    start = time.time()
    randomnum = (random.randint(2,99))
    #print(randomnum)
    print("Welcome to the Number Guessing game! \nI am thinking of a number between 1 and 100. \nYou have 5 chances to guess the correct number.")
    print("\nPlease select the difficulty level:"
          "\n1. Easy(10 chances)"
          "\n2. Medium(5 chances)"
          "\n3. Hard(3 chances)")

    difficulty = input("Enter your choice:")

    gmade = 0
    if difficulty == "1":
        totalguess = 10
        print("You have chosen Easy and have 10 chances to guess the correct number.")
        for i in range(totalguess):
            guess = int(input("Enter your guess:"))
            gmade += 1

            if guess == randomnum:
                print("\n")
                print("Congratulations, you guessed the correct number!")
                print("You made " + str(gmade) + " guesses to guess the correct number.")
                end = time.time()
                length = end - start
                print("You took", round(length), "seconds to guess.")
                break
            elif guess > 100:
                print("Sorry, you guessed too high.")

            elif guess < 0:
                print("Sorry, you guessed too low.")
            elif guess < randomnum:
                print(f"The number is greater than {guess}.")
            elif guess > randomnum:
                print(f"The number is less than {guess}.")
            if gmade == totalguess:
                print("\n")
                print("Sorry, you used up all your guesses.")
                print("You made " + str(gmade) + " guesses")

                end = time.time()
                length = end - start
                print("You took", round(length), "seconds to guess. ")
                print("The number was", randomnum)


    elif difficulty == "2":
        totalguess = 5
        print("You have chosen Medium and have 5 chances to guess the correct number.")
        for i in range(totalguess):
            guess = int(input("Enter your guess:"))
            gmade += 1

            if guess == randomnum:
                print("\n")
                print("Congratulations, you guessed the correct number!")
                print("You made " + str(gmade) + " guesses to guess the correct number.")
                end = time.time()
                length = end - start
                print("You took", round(length), "seconds to guess.")
                break
            elif guess > 100:
                print("Sorry, you guessed too high.")

            elif guess < 0:
                print("Sorry, you guessed too low.")
            elif guess < randomnum:
                print(f"The number is greater than {guess}.")
            elif guess > randomnum:
                print(f"The number is less than {guess}.")
            if gmade == totalguess:
                print("\n")
                print("\nSorry, you used up all your guesses.")

                print("You made " + str(gmade) + " guesses")

                end = time.time()
                length = end - start
                print("You took", round(length), "seconds to guess.")
                print("The number was", randomnum)
    elif difficulty == "3":
        totalguess = 3
        print("You have chosen Hard and have 3 chances to guess the correct number.")
        for i in range(totalguess):
            guess = int(input("Enter your guess:"))
            gmade += 1

            if guess == randomnum:
                print("\n")
                print("Congratulations, you guessed the correct number!")
                print("You made " + str(gmade) + " guesses to guess the correct number.")
                end = time.time()
                length = end - start
                print("You took", round(length), "seconds to guess.")
                break
            elif guess > 100:
                print("Sorry, you guessed too high.")

            elif guess < 0:
                print("Sorry, you guessed too low.")
            elif guess < randomnum:
                print(f"The number is greater than {guess}.")
            elif guess > randomnum:
                print(f"The number is less than {guess}.")
            if gmade == totalguess:
                print("\n")
                print("Sorry, you used up all your guesses.")
                print("You made " + str(gmade) + " guesses")
                end = time.time()
                length = end - start
                print("You took", round(length), "seconds to guess.")
                print("The number was", randomnum)
    else:
        print("Invalid choice")
        return
while True:
    game()
    restart = input("Do you want to restart? (y/n)")
    if restart != "y":
        break



