n = int(input())
arr = tuple(map(int, input().split()))

result = []
for i in range(n):
    result.insert(arr[i], i+1)
result.reverse()

print(*result)