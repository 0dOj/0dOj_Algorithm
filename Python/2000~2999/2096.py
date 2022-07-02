from sys import stdin
input = stdin.readline

n = int(input())

xl = list(map(int, input().split()))
nl = [xl[i] for i in range(3)]

for i in range(n-1):
    l, m, r = map(int, input().split())

    xl.extend([max(xl[0:2])+l, max(xl[0:3])+m, max(xl[1:3])+r])
    nl.extend([min(nl[0:2])+l, min(nl[0:3])+m, min(nl[1:3])+r])

    xl = xl[3:]
    nl = nl[3:]

print(max(xl), min(nl))