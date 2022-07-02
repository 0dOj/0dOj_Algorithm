import sys
input = sys.stdin.readline

K, N = map(int, input().split())
lans = []

for i in range(K):
    lans.append(int(input()))

high = sum(lans) + 1; low = 0; ans = 0

while True:
    mid = (high + low) // 2
    if mid == ans:
        break
    cnt = 0
    for i in range(K):
        cnt += lans[i] // mid
    if cnt >= N:
        ans = mid
        low = mid - 1
    elif cnt < N:
        high = mid + 1
    
print(ans)