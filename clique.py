from mip import Model, maximize, BINARY, xsum

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

model = Model()

x = [model.add_var(var_type=BINARY) for i in range(n)]

model.objective = maximize(xsum(x))

for i in range(n):
    for j in range(n):
        if i != j and g[i][j] == 0:
            model += x[i] + x[j] <= 1

model.optimize()

total = 0

for i in range(n):
    if x[i].x >= 0.99:
        total += 1
        print(i + 1, end=' ')

print()

print('Total {} vertices in clique'.format(total))
