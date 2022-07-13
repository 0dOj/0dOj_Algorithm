from sys import stdin

input = stdin.readline

n, m = map(int, input().split())
s = set()
for i in range(n):
    s.add(input().rstrip())
c = 0
for i in range(m):
    if input().rstrip() in s:
        c += 1
print(c)