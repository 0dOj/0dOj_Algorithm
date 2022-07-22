n = int(input())
arr = list(map(int, input().split()))
for i in range(n):
    arr[i] = (i, arr[i])

nge = [-1] * n

stack = []
for i in arr:
    while stack and i[1] > stack[-1][1]:
        nge[stack.pop()[0]] = i[1]
    stack.append(i)

print(*nge)