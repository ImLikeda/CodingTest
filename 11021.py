# T = int(input())
#
# for i in range (1,T+1) :
#         ai, bi = map(int,input().split())
#     print("Case #" , i,":", (ai+bi))

T = int(input())

answer = []

for i in range(T):
    ai, bi = map(int, input().split())
    answer.append(ai + bi)

for index, k in enumerate(answer):
    print(f"Case #{index + 1}: {k}")
