from collections import deque
from sys import stdin
input = stdin.readline

for i in range(int(input())):
    func = input()
    n = int(input())
    arr = deque(eval(input()))
    head = -1
    error = False
    for c in func:
        if c == "R":
            head *= -1
        if c == "D":
            try:
                if head == -1:
                    arr.popleft()
                elif head == 1:
                    arr.pop()
            except:
                error = True
                break
    if error: print("error")
    else: 
        if head == 1: arr.reverse()
        print(str(list(arr)).replace(' ',''))