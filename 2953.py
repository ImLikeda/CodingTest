n = []

for i in range(5):
    n.append(sum(map(int, input().split())))

print(n.index(max(n))+1, max(n))