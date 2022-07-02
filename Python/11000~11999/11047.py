coin = []

N, K = map(int, input().split())

for i in range(N):
    coin.append(int(input()))

coin.reverse()

count = 0

for i in range(len(coin)):
    if K >= coin[i]:
        count += (K // coin[i])
        K %= coin[i]
        if K <= 0:
            break

print(count)