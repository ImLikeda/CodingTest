a, b = map(int, input().split())
c = int(input())

if b + c < 60 :
    print(a, b+c)

elif b+c >= 60 :
    d = (b+c) // 60
    e = (b+c) % 60
    print((a+d)%24, e)