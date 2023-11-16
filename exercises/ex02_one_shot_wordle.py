"""ex02_one_shot_wordle."""

__author__ = "730660942"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

secret: str = "python"
word: str = str(input("What is your 6-letter guess?"))
index: int = 0
emoji: str = ""

while len(word) != 6:
    word = input("That was not 6 letters! Try again:")
while index < len(secret):
    if word[index] == secret[index]:
        emoji = emoji + GREEN_BOX
    else: 
        al_index: int = 0
        guessed_character = False
        while (guessed_character is not True) and (al_index < len(secret)):
            if secret[al_index] == word[index]:
                guessed_character = True
            else: 
                al_index = al_index + 1

        if guessed_character is True:
            emoji = emoji + YELLOW_BOX
        else: 
            emoji = emoji + WHITE_BOX
    
    index = index + 1
print(emoji)

if len(word) == 6:
    if word == secret:
        print("Woo! You got it!")
    else: 
        print("Not quite. Play again soon!")



    
