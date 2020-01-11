import pycosat
import sys

if len(sys.argv) >= 2:
    n = int(sys.argv[1])
else:
    n = int(input())

clauses = []

for i in range(n):
    row = []
    for j in range(n):
        for k in range(1, n):
            if k != i:
                clauses.append([-(i * n + j + 1), -(k * n + j + 1)])
            if k != j:
                clauses.append([-(i * n + j + 1), -(i * n + k + 1)])
            if i + k < n and j + k < n:
                clauses.append([-(i * n + j + 1), -((i + k) * n + j + k + 1)])
            if i - k >= 0 and j + k < n:
                clauses.append([-(i * n + j + 1), -((i - k) * n + j + k + 1)])
            if i + k < n and j - k >= 0:
                clauses.append([-(i * n + j + 1), -((i + k) * n + j - k + 1)])
            if i - k >= 0 and j - k >= 0:
                clauses.append([-(i * n + j + 1), -((i - k) * n + j - k + 1)])
        row.append(i * n + j + 1)
    clauses.append(row)

answer = pycosat.solve(clauses)
if answer == 'UNSAT':
    print('UNSOLVABLE')
else:
    for i in range(n):
        for j in range(n):
            if(answer[i * n + j] > 0):
                print('*', end='')
            else:
                print('.', end='')
        print()
