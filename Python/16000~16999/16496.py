from functools import cmp_to_key

def compare(x, y):
    if x+y > y+x:
        return -1
    elif x+y == y+x:
        return 0
    else:
        return 1

n = int(input())
arr = input().split()

arr.sort(key=cmp_to_key(compare))

print(int(''.join(arr)))