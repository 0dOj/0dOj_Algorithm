def hansoo(n):
    global cnt
    if n < 100: cnt += 1
    elif n >= 100:
        d = n//100 - n%100//10
        if d == n%100//10 - n%10: cnt += 1
cnt = 0
for i in range(1, int(input())+1):
    hansoo(i)
print(cnt)