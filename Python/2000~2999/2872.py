from sys import stdin

input = stdin.readline

n = int(input())
high = 0
ans = 0
for i in range(n):
    x = int(input())
    if x > high:
        high = x
    else:
        ans = max(ans, x)
print(ans)