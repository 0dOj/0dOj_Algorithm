n = int(input())

arr2 = [int(input())]
for i in range(1, n):

    arr1 = arr2
    arr2 = list(map(int, input().split()))

    arr2[0] += arr1[0]
    arr2[-1] += arr1[-1]
    
    for j in range(i-1):
        arr2[j+1] += max(arr1[j], arr1[j+1])

print(max(arr2))