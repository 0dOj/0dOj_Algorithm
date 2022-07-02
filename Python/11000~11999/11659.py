from sys import stdin
input = stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))

arrsum = [0]
for i in range(n):
    arrsum.append(arrsum[i]+arr[i])

for _ in range(m):
    i, j = map(int, input().split())
    print(arrsum[j]-arrsum[i-1])