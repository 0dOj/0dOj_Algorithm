from collections import deque

lst = deque([])

for i in range(int(input())):
    lst.append(i + 1)

while len(lst) != 1:
    lst.popleft()
    lst.append(lst.popleft())

print(lst[0])