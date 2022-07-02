import sys
input = sys.stdin.readline
cnt = {}
for i in range(1, 10001):
    cnt[i] = 0

N = int(input())
for i in range(N):
    cnt[int(input())] += 1

for i in range(1, 10001):
    for j in range(cnt[i]):
        print(i)