a, b, c = map(int, input().split())
d = int(input())
e = (c + d) // 60  # 초 -> 분
f = (c + d) % 60  # 분으로 바꾼 초의 나머지
i = (b + e) // 60  # 분 -> 시간
j = (b + e) % 60  # 시간으로 바꾼 분의 나머자

if c + d < 60:
    print(a, b, c + d)

elif 60 <= e < 3600:
    if (b + e) < 60:
        print(a, b + e, f)

    else:
        if a == 23:
            print('0', j, f)

        else:
            print(a + i, j, f)

else:
    if a + i > 24:
        print((a + i) - 24, j, f)

    else:
        print(a + i, j, f)
