N = int(input())
lst = ["666"]

for i in range(1, 10000):
    lst.append(str(i) + "666")
for i in range(0, 10000):
    lst.append("666" + str(i))
for i in range(0, 1000):
    lst.append("6660" + str(i))
for i in range(0, 100):
    lst.append("66600" + str(i))
for i in range(0, 10):
    lst.append("666000" + str(i))

for i in range(1, 1000):
    for j in range(0, 10):
        lst.append(str(i) + "666" + str(j))

for i in range(1, 100):
    for j in range(0, 100):
        lst.append(str(i) + "666" + str(j))
    for j in range(0, 10):
        lst.append(str(i) + "6660" + str(j))

for i in range(1, 10):
    for j in range(0, 1000):
        lst.append(str(i) + "666" + str(j))
    for j in range(0, 100):
        lst.append(str(i) + "6660" + str(j))
    for j in range(0, 10):
        lst.append(str(i)+ "66600" + str(j))

lst = list(map(int, list((set(lst)))))
lst.sort()

print(lst[N - 1])