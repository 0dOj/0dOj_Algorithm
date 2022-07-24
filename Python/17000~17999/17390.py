from sys import stdin

input = stdin.readline

n, q = map(int, input().split())
arr = sorted(map(int, input().split()))

fsum = [0]
for i in range(n):
    fsum.append(arr[i]+fsum[i])

for _ in range(q):
    a, b = map(int, input().split())
    print(fsum[b]-fsum[a-1])