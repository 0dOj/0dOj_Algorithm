n = int(input())

arr = list(map(int, input().split()))
arr.sort()

k = int(10e8)
for i in range(n):
    k = min(k, arr[i] // (i+1))
print(k)