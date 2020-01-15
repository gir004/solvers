import pycosat

n, m = map(int, input().split()[2:])

g = []
for i in range(n):
    row = []
    for j in range(n):
        row.append(0)
    g.append(row)

for i in range(m):
    u, v = map(int, input().split()[1:])
    u -= 1
    v -= 1
    g[u][v] = 1
    g[v][u] = 1

print('start solving')

for t in range(n, 0, -1):
    print(t, '/', n)
    clauses = []
    for i in range(n):
        node = []
        for k in range(t):
            node.append(i * t + k + 1)
            for j in range(n):
                if i != j and g[i][j] == 1:
                    clauses.append([-(i * t + k + 1), -(j * t + k + 1)])
        clauses.append(node)
    clauses.append([1])
    for i in range(1, n):
        clauses.append([-(i * t + 1)])
    answer = pycosat.solve(clauses)
    if(answer == 'UNSAT'):
        print('answer is', t + 1)
        break
    