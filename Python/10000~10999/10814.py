import sys
input = sys.stdin.readline

N = int(input())
lst = []

for i in range(N):
    age, name = input().split()
    lst.append([int(age), i, name])

lst.sort()

for i in range(N):
    print(lst[i][0], lst[i][2])