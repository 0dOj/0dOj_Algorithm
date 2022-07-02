n = int(input())
m = int(input())
s = input()
cnt = 0; ans = 0; need = 'I'

for i in range(m):
    if s[i] == need:
        cnt += 1
        if cnt == 2*n+1: ans += 1; cnt -= 2
        if s[i] == 'I': need = 'O'
        else: need = 'I'
    else:
        if s[i] == 'I': need = 'O'; cnt = 1
        else: need = 'I'; cnt = 0
print(ans)