input()
set1 = set(map(int, input().split()))
set2 = set(map(int, input().split()))
dif = set1 - set2
if len(dif) == 0:
    print(0)
else:
    print(len(dif))
    print(*sorted(list(dif)))