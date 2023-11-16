"""/list/ Utility Functions."""

__author__ = "730660492"


def all(numbers: list[int], integer: int) -> bool:
    """Test whether if the int in the list is the same with the given int."""
    if len(numbers) == 0:
        return False
    idx: int = 0
    while idx < len(numbers):
        if integer == numbers[idx]: 
            idx += 1
        else:
            return False
    return True    


def max(numbers: list[int]) -> int:
    """Give the largest int from the list."""
    if len(numbers) == 0:
        raise ValueError("max() arg is an empty List")
    high_number: int = numbers[0]
    idx: int = 0
    while idx < len(numbers):
        current_number: int = numbers[idx]
        if current_number > high_number:
            high_number = current_number
        idx += 1
    return high_number
    

def is_equal(list1: list[int], list2: list[int]) -> bool:
    """Test if two lists are deeply equal."""
    if len(list1) != len(list2):
        return False
    idx: int = 0
    while idx < len(list1):
        if list1[idx] == list2[idx]:
            idx += 1
        else: 
            return False
    return True