for c in range(1, int(input())+1):
    print(f'Class {c}')
    arr = sorted(map(int, input().split()[1:]))
    gap = 0
    for i in range(len(arr)-1):
        gap = max(gap, arr[i+1]-arr[i])
    print(f'Max {arr[-1]}, Min {arr[0]}, Largest gap {gap}')