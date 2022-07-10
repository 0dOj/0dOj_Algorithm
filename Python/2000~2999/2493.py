from collections import deque

n = int(input())
arr = list(map(int, input().split()))
stack = []
result = [0] * n

for i in range(n-1, -1, -1):
    while stack:
        if stack[-1][0] <= arr[i]:
            result[stack[-1][1]] = i+1
            stack.pop()
        else:
            break
    stack.append((arr.pop(), i))

print(*result)