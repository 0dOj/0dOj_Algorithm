from collections import defaultdict
from sys import stdin
input = stdin.readline

for _ in range(int(input())):
    n = int(input())
    dic = defaultdict(int)
    for i in range(n):
        s = input().split()
        dic[s[1]] += 1
    ans = 1
    for i in dic:
        ans *= dic[i]+1
    print(ans-1)