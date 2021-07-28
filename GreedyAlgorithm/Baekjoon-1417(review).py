N = int(input())
people = []
result = 0
dasom = int(input())
for _ in range(N-1):
    people.append(int(input())) 
people = sorted(people, reverse=True)
if N == 1:
    print(0)
else:
    while people[0] >= dasom:
        dasom += 1
        people[0] -= 1
        result += 1
        people = sorted(people, reverse=True)
    print(result)
