a = []
b = 0

for _ in range (9) :
    a.append(int(input()))

for i in range (9) :
    if max(a) == a[i] :
        b = i + 1

print(max(a))
print(b)