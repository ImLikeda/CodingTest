x, y = map(int, input().split())
basket = []

for _ in range (x) :
    basket.append(0)

for i in range (y) :
    a, b, c = map(int, input().split())

    for j in range(a-1, b) :
        basket[j] = c

for k in basket:
    print(k, end=' ')