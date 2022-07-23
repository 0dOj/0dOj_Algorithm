sieve = [True] * 4000001
prime = []
for i in range(2, 4000001):
    if sieve[i]:
        prime.append(i)
        for j in range(2*i, 4000001, i):
            sieve[j] = False

n = int(input())
i, j = 0, 0
sm = 0
cnt = 0
while True:
    if sm < n:
        sm += prime[j]
        j += 1
    elif sm > n:
        sm -= prime[i]
        i += 1
    elif sm == n:
        cnt += 1
        sm -= prime[i]
        i += 1
        sm += prime[j]
        j += 1
    if j >= len(prime):
        while i < len(prime):
            if sm == n:
                cnt += 1
            sm -= prime[i]
            i += 1
        break

print(cnt)