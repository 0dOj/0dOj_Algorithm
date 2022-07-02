from collections import Counter
import sys
input = sys.stdin.readline

N = int(input())
Ncards = list(map(int, input().split()))
M = int(input())
Mcards = list(map(int, input().split()))

cnt = dict(Counter(Ncards))
ans = ""

for i in range(M):
    if Mcards[i] in cnt:
        ans += str(cnt[Mcards[i]]) + " "
    else:
        ans += "0 "

print(ans)