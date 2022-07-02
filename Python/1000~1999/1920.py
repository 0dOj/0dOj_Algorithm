import sys

N = int(input())
A = list(map(int, sys.stdin.readline().split()))
M = int(input())
lst = list(map(int, sys.stdin.readline().split()))

A.sort()

for i in range(len(lst)):
    low = 0; high = len(A) - 1

    while True:
        mid = (high + low) // 2    
        if lst[i] == A[mid]:
            print("1")
            break
        if lst[i] < A[mid]:
            high = mid
        if lst[i] > A[mid]:
            low = mid
        if high - low <= 1:
            if lst[i] == A[high]:
                print("1")
                break
            elif lst[i] == A[low]:
                print("1")
                break               
            else:
                print("0")
                break