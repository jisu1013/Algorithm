def count(target, start):
  if target == 0:
    answer = [0,1,0,1,0,1]
    
  else:
    answer = [1,0,1,0,1,0]

n,m = map(int, input().split())
board = [[0] * m for _ in range(n)]
for i in range(n):
  tmp = input()
  for j in range(m):
    if tmp[j] == 'B':
      board[i][j] = 1
    else:
      board[i][j] = 0
print(board)
cnt = 64
for i in range(n-7):
  for j in range(m-7):
    if board[i][j] == 0:
      tmp = count(0, [i,j])
    else:
      tmp = count(1, [i,j])    
    cnt = min(tmp, cnt)
