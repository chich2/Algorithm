list = []

for i in range(9):
    list.append(int(input()))

num_max = sorted(list).pop()
print(num_max)
print(list.index(num_max) +1)