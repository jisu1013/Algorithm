from itertools import permutations

n = int(input())
k = int(input())
input_ = []
for _ in range(n):
  input_.append(input())
cards = list(permutations(input_, k))
result = []
for card in cards:
  tmp = ""
  for i in range(k):
    tmp += card[i] 
  result.append(tmp)
result = list(set(result))
print(len(result))
