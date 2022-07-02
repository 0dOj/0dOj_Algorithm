import sys
input = sys.stdin.readline

N, M = map(int, input().split())
trees = list(map(int, input().split()))

high = sum(trees) + 1; low = -1; ans = 0

while True:
    mid = (high + low) // 2
    if mid == ans:
        break
    cnt = 0
    for i in range(N):
        cnt += max(trees[i] - mid, 0)
    if cnt >= M:
        ans = mid
        low = mid - 1
    elif cnt < M:
        high = mid + 1
    
print(ans)