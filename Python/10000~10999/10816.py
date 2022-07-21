from collections import defaultdict

input()
arr = map(int, input().split())

dic = defaultdict(int)
for i in arr:
    dic[i] += 1

input()
arr = map(int, input().split())
ans = []
for i in arr:
    ans.append(dic[i])

print(*ans)