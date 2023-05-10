# 2588
# / 는 소수점 포함, // 소수점 미포함, %는 나머지


a = int(input())
b = int(input())

c = b%10            # 마지막 수
d = (b%100)//10     # 두번째 수
e = b//100          # 첫번째 수

print(c*a)
print(d*a)
print(e*a)
print(a*b)


