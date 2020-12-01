# Marcin Kapiszewski

def check_vertise(a, b, change, i, j):

    if (a + i, b + j) in vertices:
        vertices.remove((a + i, b + j))
        if a + i == 1 or b + j == 1:
            return change
        return change - 2
    else:
        vertices.add((a + i, b + j))
        return change


def repear_result(i1, j1, i2, j2):
    if i1 == 1:
        if j1 == 1:
            change = 1
        else:
            change = 2
    elif j1 == 1:
        change = 2
    else:
        change = 4

    change = check_vertise(i1, j1, change, 0, 0)
    change = check_vertise(i1, j2, change, 0, 1)
    change = check_vertise(i2, j1, change, 1, 0)
    change = check_vertise(i2, j2, change, 1, 1)

    return change


if __name__ == "__main__":
    n, m, q = map(int, input().split())
    vertices = set()
    result = 0
    for _ in range(q):
        data = map(int, input().split())
        result += repear_result(*data)
        print(result)
