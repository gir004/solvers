from itertools import product

for x1, x2, x3 in product((0, 1), repeat=3):
    x4 = (x2 + x3) % 2
    x5 = (x1 + x4) % 2
    x6 = x2 * x3
    x7 = x1 * x4
    x8 = (x6 + x7) % 2

    assert x1 + x2 + x3 == x5 + 2 * x8
