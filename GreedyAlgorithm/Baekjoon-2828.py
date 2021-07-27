n, m = map(int, input().split())
j = int(input())
apples = []

for _ in range(j):
  apples.append(int(input()))

start = 1
end = start + m - 1
result = 0
move = 0

for apple in apples:
  move = 0
  if apple > end:
    move = apple - end
    end = apple
    start += move
  elif apple < start:
    move = start - apple
    start = apple
    end -= move
  result += move
  
print(result)

###그 전 오답
n, m = map(int, input().split())
j = int(input())
apples = []
for _ in range(j):
    apples.append(int(input()))
result = 0
pos = 1
move = 0
for apple in apples:
    move = 0
    if apple > (pos + m):
        move = apple - (pos+m-1)
        pos += move
    elif apple < pos:
        move = pos - apple
        pos -= move  
    result += move
print(result)
