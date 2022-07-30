from collections import defaultdict
from sys import stdin

input = stdin.readline

dic = defaultdict(int)
n = int(input())
for _ in range(n):
    dic[input().rstrip()] += 1
for _ in range(n-1):
    dic[input().rstrip()] -= 1
for i in dic:
    if dic[i]:
        print(i)
        break