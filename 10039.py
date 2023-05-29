a, b, c, d, e = map(int, input().split())
n = [a, b, c, d, e]

for i in range(4):
    if n[i] < 40:
        n[i] = 40

    i += 1

p = (n[0] + n[1] + n[2] + n[3] + n[4]) // 5

print(p)
