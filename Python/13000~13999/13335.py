from collections import deque

n, w, l = map(int, input().split())
arr = deque(map(int, input().split()))

q = deque([0] * w)
time = 0
while arr:
    time += 1
    q.popleft()
    q_sum = sum(q)
    if q_sum+arr[0] <= l:
        q.append(arr.popleft())
    else:
        q.append(0)
print(time+w)