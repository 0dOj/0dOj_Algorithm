m = int(input())
input()
cnt_set = set(map(int, input().split()))
mx = max(cnt_set)

win_arr = [False]

i = 1

while i <= 2000:
    win_arr.append(False)

    for cnt in cnt_set:
        if i-cnt >= 0 and not win_arr[i-cnt]:
            win_arr[i] = True
            break

    if i == m:
        cywin = 0
        for i in win_arr[1:]:
            if not i:
                cywin += 1
        print(cywin)
        exit(0)

    i += 1

for i in range(mx+1, 1000):
    if win_arr[len(win_arr)-i:] == win_arr[len(win_arr)-i*2:len(win_arr)-i]:
        cycle = win_arr[len(win_arr)-i:]
        idx = len(win_arr)-i
        break

cywin = 0

for i in win_arr[1:idx]:
    if not i:
        cywin += 1

m -= len(win_arr[1:idx])

cywin_in_cycle = 0

for i in cycle:
    if not i:
        cywin_in_cycle += 1

cywin += m//len(cycle)*cywin_in_cycle
m %= len(cycle)

for i in range(m):
    if not cycle[i]:
        cywin += 1

print(cywin)