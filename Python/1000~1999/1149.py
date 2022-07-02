from sys import stdin
input = stdin.readline

n = int(input())

arr = list(map(int, input().split()))

for i in range(1, n):
    r, g, b = map(int, input().split())
    mnr = min(arr[1], arr[2])+r
    mng = min(arr[2], arr[0])+g
    mnb = min(arr[0], arr[1])+b
    arr = [mnr, mng, mnb]

print(min(arr))