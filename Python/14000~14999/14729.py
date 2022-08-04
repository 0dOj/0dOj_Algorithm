from sys import stdin

input = stdin.readline

lst = []

for _ in range(int(input())):
    lst.append(float(input()))
lst.sort()
    
for i in range(7):
    print(f'{lst[i]:0.3f}')