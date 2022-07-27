from sys import stdin
from collections import defaultdict

input = stdin.readline

n = int(input())
dic = defaultdict(int)

for i in range(n):
    dic[int(input())] += 1

mx = 0
ans = 0
for i in sorted(dic.keys()):
    if dic[i] > mx:
        mx = dic[i]
        ans = i
print(ans)