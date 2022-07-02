import sys

while True:
    lst = list(map(int, sys.stdin.readline().split()))
    if lst == []:
        break
    else:
        print(sum(lst))