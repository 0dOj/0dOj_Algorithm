n = int(input())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

row1 = 0
row2 = 0
max_row1 = 0
max_row2 = 0
for i in range(n):
    if arr1[i] - arr2[i] == 1 or arr1[i] - arr2[i] == -2:
        row1 += 1
        row2 = 0
        max_row1 = max(row1, max_row1)
    elif arr1[i] - arr2[i] == -1 or arr1[i] - arr2[i] == 2:
        row2 += 1
        row1 = 0
        max_row2 = max(row2, max_row2)
    else:
        if row1 == 0:
            row1 = 1
            row2 = 0
        else:
            row1 = 0
            row2 = 1

print(max(max_row1, max_row2))