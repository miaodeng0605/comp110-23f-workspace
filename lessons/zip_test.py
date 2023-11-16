"""Test my zip function."""

__author__ = "730660492"


from lessons.zip import zip


def test_empty_zip() -> None:
    """Testing on a dictionary with one empty list."""
    assert zip([], []) == {}


def test_zip_1() -> None:
    """Testing a dictionary."""
    test_dictionary: dict[str, int] = {"Serena": 100}
    assert zip(["Serena"], [100]) == test_dictionary


def test_zip_2() -> None:
    """Testing a dictionary."""
    test_dictionary: dict[str, int] = {"Serena": 100, "Miao": 100}
    assert zip(["Serena", "Miao"], [100, 100]) == test_dictionary
