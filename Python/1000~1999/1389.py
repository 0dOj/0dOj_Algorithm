from collections import defaultdict

dic = defaultdict(int)

n = int(input())
for i in range(n):
    s = input()[::-1]
    for j in range(len(s)):
        dic[s[j]] += 10 ** j

dicvals = sorted(dic.values(), reverse=True)

result = 0
for i in range(len(dicvals)):
    result += dicvals[i] * (9-i)

print(result)