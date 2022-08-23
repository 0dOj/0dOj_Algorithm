n = int(input())
s = input()

l_cnt = 0
s_cnt = 0
cnt = 0

for c in s:
    if c == 'L':
        l_cnt += 1
    elif c == 'R':
        if l_cnt:
            cnt += 1
            l_cnt -= 1
        else:
            break
    elif c == 'S':
        s_cnt += 1
    elif c == 'K':
        if s_cnt:
            cnt += 1
            s_cnt -= 1
        else:
            break
    else:
        cnt += 1

print(cnt)