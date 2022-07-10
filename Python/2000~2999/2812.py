from collections import deque

n, k = map(int, input().split())
s = input()

queue = deque([(s[0], 0)])
remove_list = []
for i in range(1, n):
    while len(queue) != 0 and s[i] > queue[-1][0]:
        remove_list.append(queue.pop()[1])
    if len(remove_list) >= k:
        break
    queue.append((s[i], i))
while len(remove_list) < k:
    remove_list.append(queue[-1][1])
    queue.pop()

remove_set = set(remove_list[:k])
ans = ''
for i in range(n):
    if not i in remove_set:
        ans += s[i]

print(ans)