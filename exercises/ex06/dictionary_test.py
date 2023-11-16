"""Unit test for dictionary functions."""

__author__ = "730660942"


from exercises.ex06.dictionary import invert
from exercises.ex06.dictionary import favorite_color
from exercises.ex06.dictionary import count
from exercises.ex06.dictionary import alphabetizer
from exercises.ex06.dictionary import update_attendance
import pytest 


def test_empty_invert() -> None:
    """Testing on a invert dictionary with one empty dictionary."""
    empty_dictionary: dict[str, str] = {"": ""}
    assert invert(empty_dictionary) == {"": ""}


with pytest.raises(KeyError):
    my_dictionary = {"Serena": "4.0", "Miao": "4.0"}
    invert(my_dictionary)


def test_invert_1() -> None:
    """Testing the function of inverting dictionary."""
    test_invert_dictionary: dict[str, str] = {"4.0": "Serena"}
    assert invert(test_invert_dictionary) == {"Serena": "4.0"}


def test_invert_2() -> None:
    """Testing the function of inverting dictionary."""
    test_invert_dictionary: dict[str, str] = {"Serena": "cornell"}
    assert invert(test_invert_dictionary) == {"cornell": "Serena"}


def test_empty_favorite_color() -> None:
    """Testing on favorite color with one empty dictionary."""
    test_favorite_color_dict: dict[str, str] = {}
    assert favorite_color(test_favorite_color_dict) == ""


def test_favorite_color_1() -> None:
    """Testing the favorite color."""
    test_favorite_color_dict: dict[str, str] = {"Serena": "purple", "Miao": "purple", "Deng": "red"}
    assert favorite_color(test_favorite_color_dict) == "purple"


def test_favorite_color_2() -> None:
    """Testing the favorite color."""
    test_favorite_color_dict: dict[str, str] = {"Serena": "red", "Miao": "purple", "Deng": "red"}
    assert favorite_color(test_favorite_color_dict) == "red"


def test_favorite_color_3() -> None:
    """Testing the favorite color."""
    test_favorite_color_dict: dict[str, str] = {"Serena": "blue", "Miao": "purple", "Deng": "blue"}
    assert favorite_color(test_favorite_color_dict) == "blue"


def empty_count() -> None:
    """Testing with an empty list."""
    test_count_list: list[str] = []
    assert count(test_count_list) == int()


def test_count1() -> None:
    """Testing on a counting function."""
    test_count_list: list[str] = ["serena", "serena", "serena", "4.0", "4.0"]
    assert count(test_count_list) == {"serena": 3, "4.0": 2}


def test_count2() -> None:
    """Testing on a counting function."""
    test_count_list: list[str] = ["serena", "serena", "serena", "4.0", "4.0", "4.0"]
    assert count(test_count_list) == {"serena": 3, "4.0": 3}


def test_count3() -> None:
    """Testing on a counting function."""
    test_count_list: list[str] = ["serena", "serena", "serena", "4.0", "4.0", "4.0", "4.0"]
    assert count(test_count_list) == {"serena": 3, "4.0": 4}


def test_empty_alphabetizer() -> None:
    """Testing on an empty alphabetizer dictionary."""
    test_empty_alphabetizer: list[str] = []
    assert alphabetizer(test_empty_alphabetizer) == {}


def test_alphabetizer1() -> None:
    """Testing on a alphabetizer dictionary."""
    test_alphabetizer_list: list[str] = ["serena", "slay", "best"]
    assert alphabetizer(test_alphabetizer_list) == {"s": ["serena", "slay"], "b": ["best"]}


def test_alphabetizer2() -> None:
    """Testing on a alphabetizer dictionar."""
    test_alphabetizer_list: list[str] = ["serena", "slay", "best", "andre"]
    assert alphabetizer(test_alphabetizer_list) == {"s": ["serena", "slay"], "b": ["best"], "a": ["andre"]}




def test_alphabetizer3() -> None:
    """Testing on a alphabetizer dictionary."""
    test_alphabetizer_list: list[str] = ["serena", "slay", "best", "andre", "ai"]
    assert alphabetizer(test_alphabetizer_list) == {"s": ["serena", "slay"], "b": ["best"], "a": ["andre", "ai"]}


def test_empty_attendence() -> None:
    """Testing on an empty attendence log!!!"""
    attendence_log: dict[str, list[str]] = {"": [""]}
    day: str = ""
    student: str = ""
    assert update_attendance(attendence_log, day, student) == {"": [""]}


def test_update_attendence1() -> None:
    """Testing on an upadte attendence."""
    attendence_log: dict[str, list[str]] = {"Monday": ["Serena", "Andre"]}
    day: str = "Monday"
    student: str = "Chu"
    assert update_attendance(attendence_log, day, student) == {"Monday": ["Serena", "Andre", "Chu"]}


def test_update_attendence2() -> None:
    """Testing on an upadte attendence."""
    attendence_log: dict[str, list[str]] = {"Tuesday": ["Serena", "Andre"]}
    day: str = "Tuesday"
    student: str = "Chu"
    assert update_attendance(attendence_log, day, student) == {"Tuesday": ["Serena", "Andre", "Chu"]}


def test_update_attendence3() -> None:
    """Testing on an upadte attendence."""
    attendence_log: dict[str, list[str]] = {"Wednesday": ["Serena", "Andre"]}
    day: str = "Wednesday"
    student: str = "Chu"
    assert update_attendance(attendence_log, day, student) == {"Wednesday": ["Serena", "Andre", "Chu"]}