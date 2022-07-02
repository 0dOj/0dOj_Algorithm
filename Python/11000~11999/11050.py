import sys
input = sys.stdin.readline

N, K = map(int, input().split())
ans = 1

for i in range(K):
    ans *= N - i
    ans //= i + 1

print(ans)