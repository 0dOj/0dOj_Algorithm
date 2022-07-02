from collections import deque
from sys import stdin
input = stdin.readline

for _ in range(int(input())):
    n, t = map(int, input().split())
    visit = [''] * 10000
    queue = deque([n])
    while not visit[t]:
        x = queue.popleft()
        s = str(x).zfill(4)

        order = (
        (x * 2 % 10000, 'D'), # 1번 명령어(D)
        ((x + 9999) % 10000, 'S'), # 2번 명령어(S)
        (int(s[1:4] + s[0]), 'L'), # 3번 명령어(L)
        (int(s[3] + s[0:3]), 'R') # 4번 명령어(R)
        )

        for i in order:
            if not visit[i[0]] and i[0] != n:
                visit[i[0]] = visit[x] + i[1]
                queue.append(i[0])

    print(visit[t])