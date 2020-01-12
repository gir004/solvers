import pycosat

n, m = map(int, input('Enter a height and width of crossword: ').split())

print('Enter values for rows:')
rows = []
for i in range(n):
    rows.append(map(int, input().split()))

print('Enter values of columns:')
cols = []
for i in range(m):
    cols.append(map(int, input().split()))

clauses = []


def to_n(x, y):
    return x * m + y + 1

def from_n(x):
    return (x - 1) / m, (x - 1) % m

#TODO