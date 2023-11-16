def f(x: list[str]) -> str:
    for y in range(0, len(x)):
        x[y] += "x"
    return x[y]

def g(x: list[str]) -> list[str]:
    new_list: list[str] = []
    for z in x:
        new_list.append(str(z))
    return new_list

record: list[str] = ["x", "y"]
print(f(record))
print(g(record))