import pycosat

n, m = map(int, input().split())

field = []

for i in range(n):
    field.append(input())

clauses = []


def to_n(x, y):
    return x * m + y + 1


def from_n(x):
    return (x - 1) // m, (x - 1) % m


for i in range(n):
    for j in range(m):
        if field[i][j] == 'X':
            clauses.append([to_n(i, j)])
        elif field[i][j] == 'O':
            clauses.append([-to_n(i, j)])

for i in range(n):
    for j in range(m - 3):
        clauses.append([to_n(i, j), 
                        to_n(i, j + 1), 
                        to_n(i, j + 2), 
                        to_n(i, j + 3)])
        clauses.append([-to_n(i, j),
                        -to_n(i, j + 1),
                        -to_n(i, j + 2),
                        -to_n(i, j + 3)])

for i in range(n - 3):
    for j in range(m):
        clauses.append([to_n(i, j),
                        to_n(i + 1, j),
                        to_n(i + 2, j),
                        to_n(i + 3, j)])
        clauses.append([-to_n(i, j),
                        -to_n(i + 1, j),
                        -to_n(i + 2, j),
                        -to_n(i + 3, j),])

for i in range(n - 3):
    for j in range(m - 3):
        clauses.append([to_n(i, j),
                        to_n(i + 1, j + 1),
                        to_n(i + 2, j + 2),
                        to_n(i + 3, j + 3),])
        clauses.append([-to_n(i, j),
                        -to_n(i + 1, j + 1),
                        -to_n(i + 2, j + 2),
                        -to_n(i + 3, j + 3),])

for i in range(n - 3):
    for j in range(m - 3):
        clauses.append([to_n(i + 3, j),
                        to_n(i + 2, j + 1),
                        to_n(i + 1, j + 2),
                        to_n(i, j + 3),])
        clauses.append([-to_n(i + 3, j),
                        -to_n(i + 2, j + 1),
                        -to_n(i + 1, j + 2),
                        -to_n(i, j + 3),])

answer = pycosat.solve(clauses)

if answer == 'UNSAT':
    print('UNSOLVABLE')
else:
    print('>------------------------------')
    field = []
    for i in range(n):
        field.append([' ' for j in range(m)])
    for i in answer:
        if i > 0:
            x, y = from_n(i)
            field[x][y] = 'X'
        else:
            x, y = from_n(-i)
            field[x][y] = 'O'
    for i in range(n):
        for j in range(m):
            print(field[i][j], end='')
        print()