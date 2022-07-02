lst = [[chr(65+i), 0] for i in range(10)]
cant0 = []


n = int(input())
for i in range(n):
    s = input()[::-1]
    for j in range(len(s)):
        lst[ord(s[j])-65][1] += 10 ** j
    cant0.append(s[-1])

lst.sort(key=lambda x:x[1], reverse=True)

k = 9
while lst[k][0] in cant0:
    k -= 1
lst.append(lst.pop(k))


result = 0
for i in range(10):
    result += lst[i][1] * (9-i)

print(result)