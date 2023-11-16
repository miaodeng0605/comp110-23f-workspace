"""Dictionary functions."""

__author__ = "730660942"


def invert(d: dict[str, str]) -> dict[str, str]:
    """Inverting the keys and values of a dictionary."""
    inverted_d: dict[str, str] = {}
    for key in d:
        if d[key] in inverted_d:
            raise KeyError("error message of your choice here!")
        else:
            inverted_d[d[key]] = key
    return inverted_d


def favorite_color(c: dict[str, str]) -> str:
    """Finding the color that appears most frequntly."""
    color_list: list[str] = []
    for name in c:
        color_list.append(c[name])
    color_count = count(color_list)
    number: int = 0
    fav_color: str = ""
    for color in color_count:
        if color_count[color] > number:
            number = color_count[color]
            fav_color = color
    return fav_color


def count(count: list[str]) -> dict[str, int]:
    """Count the frequency of each item in the given list."""
    count_dict: dict[str, int] = {}
    for item in count:
        if item in count_dict:
            count_dict[item] += 1
        else:
            count_dict[item] = 1
    return count_dict


def alphabetizer(words: list[str]) -> dict[str, list[str]]:
    """Giving a list of words that belong to a given letter."""
    result_dict: dict[str, list[str]] = {}
    for word in words:
        first_letter = word[0].lower()
        if first_letter in result_dict:
            result_dict[first_letter].append(word)
        else:
            result_dict[first_letter] = [word]
    return result_dict


def update_attendance(attendence_log: dict[str, list[str]], day: str, student: str) -> dict[str, list[str]]:
    """Updating the attendence dictionary with the student's attendence on a given day."""
    if day in attendence_log:
        if student not in attendence_log[day]:
            attendence_log[day].append(student)
    else:
        attendence_log[day] = [student]
    return attendence_log
