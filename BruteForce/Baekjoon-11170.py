T = int(input())
for _ in range(T):
  cnt = 0
  n,m = map(int, input().split())
  for i in range(n,m+1):
    tmp = list(str(i))
    #print(tmp)
    for j in range(len(tmp)):
      if tmp[j] == '0':
        cnt += 1
  print(cnt)
