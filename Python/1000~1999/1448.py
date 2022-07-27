from sys import stdin

input = stdin.readline

n = int(input())
arr = sorted([int(input()) for _ in range(n)])

while len(arr) > 2:
    if arr[-1] < arr[-2] + arr[-3]:
        print(sum([arr[-i] for i in range(1, 4)]))
        exit(0)
    arr.pop()
print(-1)