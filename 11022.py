a = int(input())

answer = []

for i in range(1, a+1):
    bi, ci = map(int, input().split())
    answer.append(f"Case #{i}: {bi} + {ci} = {bi + ci}")

for value in answer:
    print(value)
