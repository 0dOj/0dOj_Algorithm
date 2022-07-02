import sys
from collections import deque
input = sys.stdin.readline

T = int(input())

for i in range(T):
    N, M = map(int, input().split())
    queue = list(map(int, input().split()))
    pos = M
    cnt = 1

    while True:
        if len(queue) != 1:
            if queue[0] >= max(queue[1:len(queue)]):
                if pos == 0:
                    print(cnt)
                    break
                else:
                    pos -= 1
                queue.pop(0)
                cnt += 1
            else:
                if pos == 0:
                    pos = len(queue) - 1
                else:
                    pos -= 1
                queue.append(queue.pop(0))
        else:
            print(cnt)
            break