a = int(input())
for i in range (a):

    b = list(input().split())
    b[0] = float(b[0])

    for j in range (len(b)) :

        if b[j] == '@' :
            b[0] = b[0] * 3

        elif b[j] == '%' :
            b[0] = b[0] + 5

        elif b[j] == '#' :
            b[0] = b[0] - 7


    print('%0.2f' % b[0])

i += 1

