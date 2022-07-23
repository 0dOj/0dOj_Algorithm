from sys import stdin

input = stdin.readline

for _ in range(int(input())):
    n = int(input())
    arr = input().split()
    s = ''
    for i in range(n):
        if s+arr[i] < arr[i]+s:
            s = s+arr[i]
        else:
            s = arr[i]+s
    print(s)