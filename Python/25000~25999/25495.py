n = int(input())
arr = tuple(map(int, input().split()))

battery = 0
linked = None
cnt = 1
for i in arr:
    if i == linked:
        cnt += 1
    else:
        cnt = 1
    battery += 2 ** cnt
    if battery >= 100:
        battery = 0
        linked = None
    else:
        linked = i

print(battery)