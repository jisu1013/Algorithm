from collections import deque

def bfs(y, x):
    for dy, dx in d:
        Y, X = y+dy, x+dx
        if (0 <= Y < R) and (0 <= X < C):
            if graph[Y][X] == 'S':
                return False
            if graph[Y][X] == '.':
                graph[Y][X] = 'D'
    return True

R, C = map(int, input().split())
graph = [list(input()) for _ in range(R)]
d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
for i in range(R):
    for j in range(C):
        t = True
        if graph[i][j] == 'W':
            t = bfs(i, j)
            if t == False:
                print(0)
                break
if t:
    print(1)
    for line in graph:
        print(''.join(line))
