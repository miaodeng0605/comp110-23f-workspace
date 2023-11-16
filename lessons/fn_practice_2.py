def mimic(my_words:str,letter_idx:int) -> str:
    """""Outputs the character of my_words at index letter_idx"""
    if letter_idx >= len(my_words):
        return("Too high of an index")
    return my_words[letter_idx]

my_words: str = input("input a word:")
letter_idx: int = int(input("input an integer:"))
mimic(my_words,letter_idx)
print(mimic(my_words,letter_idx))
