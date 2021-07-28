N = input()
left = 0
right = 0
length = len(N) // 2
for i in range(length):
  left += int(N[i])
  right += int(N[i+length])
if left == right:
  print('LUCKY')
else:
  print('READY')
