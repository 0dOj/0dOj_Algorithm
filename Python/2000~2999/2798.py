import sys
input = sys.stdin.readline

N, M = map(int, input().split())
cards = list(map(int, input().split()))
ans = 0

for i in range(N):
    c1 = cards[i]
    if c1 <= M:
        for j in range(i + 1, N):
            c2 = cards[j]
            if c1 + c2 <= M:
                for k in range(j + 1, N):
                    c3 = cards[k]
                    if ans < c1 + c2 + c3 <= M:
                        ans = c1 + c2 + c3

print(ans)