from sys import stdin
from collections import deque
input = stdin.readline

for i in range(int(input())):
    lst = deque([1,1,1,2,2])
    for i in range(int(input())-1):
        lst.append(lst[0]+lst[4])
        lst.popleft()
    print(lst[0])