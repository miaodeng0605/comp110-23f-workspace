"""Practice importing from other modules"""

from lessons.my_functions import addition
from random import randint
if __name__ == "__main__":
    print("Howdy")

print(addition(1,2))