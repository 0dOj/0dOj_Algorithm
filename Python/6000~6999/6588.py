from sys import stdin

input = stdin.readline

sieve = [True] * 1000001
prime = []
for i in range(2, 1000001):
    if sieve[i]:
        prime.append(i)
        for j in range(2*i, 1000001, i):
            sieve[j] = False
prime.pop(0)
prime_set = set(prime)

while True:
    n = int(input())
    if n == 0:
        exit(0)
    else:
        for a in prime:
            if n - a in prime_set:
                print(f'{n} = {a} + {n-a}')
                break