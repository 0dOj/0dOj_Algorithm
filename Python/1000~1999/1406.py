from sys import stdin
from collections import deque

input = stdin.readline

left = deque(input().rstrip())
right = deque()

for _ in range(int(input())):
    order = input().split()

    if order[0] == 'L':
        if left: right.appendleft(left.pop())

    elif order[0] == 'D':
        if right: left.append(right.popleft())

    elif order[0] == 'B':
        if left: left.pop()

    elif order[0] == 'P':
        left.append(order[1])

print(''.join(left+right))