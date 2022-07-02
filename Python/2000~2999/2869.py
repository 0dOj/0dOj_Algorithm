import sys
A, B, V = map(int, input().split())

climb = A - B; goal = V - A;

if V == A:
    print("1")
else:
    if goal % climb == 0:
        day = goal // climb
    else:
        day = goal // climb + 1
    print(day + 1)