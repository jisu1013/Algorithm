from collections import deque

def bfs(y,x):
  q = deque()
  q.append((y,x))
  graph[y][x] = '1'
  while q:
    y,x = q.popleft()
    for dy,dx in d:
      Y,X = y+dy, x+dx
      if (0 <= Y < R) and (0 <= X < C) and (graph[Y][X] == '#'):
        q.append((Y,X))
        graph[Y][X] = '1'

R, C = map(int, input().split())
graph = [list(input()) for _ in range(R)]
d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
cnt = 0
for i in range(R):
  for j in range(C):
    if graph[i][j] == '#':
      bfs(i,j)
      cnt += 1
print(cnt)
