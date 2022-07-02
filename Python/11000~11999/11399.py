import sys
input = sys.stdin.readline

N = int(input())
time = list(map(int, input().split()))
time.sort()
ans = 0

for i in range(N):
    ans += time[i] *  (N - i)

print(ans)