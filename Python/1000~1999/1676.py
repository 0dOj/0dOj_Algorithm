n = int(input())

cnt2 = 0; cnt5 = 0
for i in range(1, n+1):
    t = i
    while t % 2 == 0:
        cnt2 += 1
        t //= 2
    while t % 5 == 0:
        cnt5 += 1
        t //= 5
print(min(cnt2, cnt5))