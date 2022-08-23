from collections import Counter

n = int(input())
arr = list(map(int, input().split()))

table = [-2]
while arr:
    arr = sorted(arr)
    if table[-1]+1 == arr[0]:
        for i in range(len(arr)):
            if arr[i] != arr[0]:
                table.append(arr.pop(i))
                break
    elif len(Counter(arr)) == 2:
        if arr[0]+1 == arr[-1]:
            table.append(arr.pop())
        else:
            table.append(arr.pop(0))
    else:
        table.append(arr.pop(0))

print(*table[1:])