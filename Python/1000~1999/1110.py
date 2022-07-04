n = int(input())

t = n
cnt = 0
while True:
    cnt += 1
    t = int(str(t)[-1])*10 + sum(map(int, list(str(t))))%10
    if t == n:
        break

print(cnt)