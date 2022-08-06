import random
import word_list
import hangman_art

chosen_word = random.choice(word_list.word_list)
word_length = len(chosen_word)

lives = 6

print(hangman_art.logo3)

gaps = []
for _ in range(word_length):
    gaps += "_"
print(*gaps)

end_of_game = False

while end_of_game == False:

    guess = input("Guess a letter: ").lower()

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            gaps[position] = letter

    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose")

    print(f"{' '.join(gaps)}")

    if "_" not in gaps:
        end_of_game = True
        print(hangman_art.logo2)

    print(hangman_art.stages[lives])
