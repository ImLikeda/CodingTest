# for i in range(1, 51):
#     if not i % 3 == 0 :
#         i += 1
#         continue
#
#     print(i)
#     i += 1
#
#     if not i % 5 == 0 :
#         i += 1
#         continue
#
#     print(i)
#     i += 1


#for i in range(1, 51):
#    if i % 3 == 0 or i % 5 == 0:
#        print(i)

for i in range(1, 51):
    if i % 3 == 0 and i % 5 == 0 :
        print(i)