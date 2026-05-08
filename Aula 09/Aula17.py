lst = [0, 1, 4, 6, 8, 10]
print(lst)

lst2 = []
for i in range(6):
    lst2.append(i ** 2)
print(lst2)

lst3 = [i ** 2 for i in range(6)]
print(lst3)