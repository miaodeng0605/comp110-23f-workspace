"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730660942"

count: int = 0
word: str = input("Enter a 5-character word:")
if len(word) == 5:
    character: str = input("Enter a single character:")
    if len(character) == 1:
        print("Searching for " + character + " in " + word)
        if word[0] == character:
            print(character + " found at index 0")
            count += 1
        if word[1] == character:
            print(character + " found at index 1")
            count += 1
        if word[2] == character:
            print(character + " found at index 2")
            count += 1
        if word[3] == character:
            print(character + " found at index 3")
            count += 1
        if word[4] == character:
            print(character + " found at index 4")
            count += 1
        if count == 0:
            print("No instances of " + character + " found in " + word)
        if count == 1:
            print("1 instance of " + character + " found in " + word)
        if count > 1:
            print(str(count) + " instances of " + character + " found in " + word)
    else: 
        print("Error: Character must be a single character.")
        exit()
else: 
    print("Error: Word must contain 5 characters")
    exit()