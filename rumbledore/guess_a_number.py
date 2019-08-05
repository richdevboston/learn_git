import random

is_playing = True
score = 0
number_of_guesses = 3
min_num = 1
max_num = 20

while is_playing:

    rnd_num = random.randint(min_num, max_num + 1)
    print("---------- Welcome to Rumblesore's guess game ----------")

    while number_of_guesses > 0:
        answer = int(input(f"Guess a number between {min_num}-{max_num}: \n"))

        if rnd_num == answer:
            print("You guessed right!")
            score += 1

        else:
            print("Incorrect!")
            number_of_guesses -= 1
            if not number_of_guesses > 0:
                break

            if answer > rnd_num:
                print("guess lower")
            else:
                print("guess higher")

    answer = input("Wanna play again? (yes/no)\n")
    if answer == "yes":
        number_of_guesses = 3
        continue
    else:
        is_playing = False

