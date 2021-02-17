# https://www.codewars.com/kata/5a667236145c462103000091
from math import sqrt


def square_sums(num):
    def hamilton(g, size, pt, path: list):
        if pt not in set(path):
            path.append(pt)
            if len(path) == size:
                return path
            for pt_next in g.get(pt, []):
                res_path = path[:]
                candidate = hamilton(g, size, pt_next, res_path)
                if candidate is not None:
                    return candidate
    d = dict()
    for i in range(1, num + 1):
        d[i] = list()
        for j in range(1, num + 1):
            if sqrt((i + j)) % 1 == 0 and i != j:
                d[i].append(j)
    for i in range(1, num + 1):
        f = hamilton(d, num, i, [])
        if f and len(f) == num:
            return f
    return False


print(square_sums(15))
