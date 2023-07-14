a = input()
b = list(a)
c = 0

b = ['6' if a == '9' else a for a in b]

for i in range(0, 9) :
    if i == 6 :
        if b.count('6') >= 2 :
            if (b.count('6') // 2) == (b.count('6') / 2) :
                c = (b.count('6')//2) + c

            else :
                c = (b.count('6')//2) + c + 1

    elif b.count(str(i)) >= 2 :
        if c >= b.count(str(i)) :
            d = c - b.count(str(i))
            c = c + d

        else :
            c = c + b.count(str(i))

    elif i == 8:
        if c == 0:
            c = 1

print(c)
