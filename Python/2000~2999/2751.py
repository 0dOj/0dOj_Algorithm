import sys
input = sys.stdin.readline

T = int(input())
lst = []

for i in range(T):
    
    lst.append(int(input()))

lst.sort()

for i in range(len(lst)):
    print(lst[i])