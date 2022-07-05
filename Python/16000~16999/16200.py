n = int(input())
arr = list(map(int, input().split()))

arr.sort()

lim = arr[0]
man = 0
team = 1
for i in range(n):
    if man < lim:
        man += 1
    else:
        team += 1
        lim = arr[i]
        man = 1

print(team)