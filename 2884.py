a, b = map(int, input().split())
c = b - 45

if c < 0:
    b = c + 60

    if a == 0:
        a = 23
        print(a, b)

    else:
        a = a - 1
        print(a, b)

else:
    print(a, c)
