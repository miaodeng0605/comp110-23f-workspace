"""Sum all the elements of the input."""


def w_sum(vals: list[float]) -> float:
    """Sum all the elements of the input."""
    idx: int = 0
    num: float = 0.0
    while idx < len(vals):
        num += vals[idx]
        idx += 1
    return num
 

def f_sum(vals: list[float]) -> float:
    """Sum all the elements of the input."""
    add: float = 0.0
    for elem in vals:
        add += elem
    return add


def f_range_sum(vals: list[float]) -> float:
    """Sum all the elements of the output."""
    add: float = 0.0
    for idx in range(0, len(vals)):
        add += vals[idx]
    return add
