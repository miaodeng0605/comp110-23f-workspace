"""Structured Wordle."""

__author__ = "730660492"


def contains_char(word: str, character: str) -> bool:
    """Finding character in word."""
    assert len(character) == 1
    index: int = 0
    while index < len(word):
        if word[index] == character:
            return True
        index += 1
    return False


def emojified(guess: str, secret: str) -> str:
    """Test green, yellow or white box.""" 
    assert len(guess) == len(secret)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    emoji = ""
    index2: int = 0
    while index2 < len(secret):
        if guess[index2] == secret[index2]:
            emoji += GREEN_BOX
        elif contains_char(secret, guess[index2]) is True:
            emoji += YELLOW_BOX
        else:
            emoji += WHITE_BOX
        index2 += 1
    return (emoji)


def input_guess(expected_length: int) -> str:
    """Test expected length of guess."""
    guess: str = input(f"Enter a {expected_length} character word: ")
    while len(guess) != expected_length:
        new_guess: str = input(f"That wasn't {expected_length} chars! Try again: ")
        guess = new_guess
    return guess


def main() -> None:
    """The entrypoint of the program and main game loop."""
    turn = 1
    secret = str("codes")
    while turn < 7:
        print(f"=== Turn {turn}/6 ===")
        guess: str = input_guess(len(secret))
        print(emojified(guess, secret))
        if guess == secret:
            print(f"You won in {turn}/6 turns!")
            return None
        turn += 1
    print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main()