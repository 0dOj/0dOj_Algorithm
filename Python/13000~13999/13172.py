import math

mod = 1000000007

n = int(input())

def fpow(c, n):
    if n == 1:
        return c
    else:
        x = fpow(c, n//2)
        if n%2 == 0:
            return x * x % mod
        else:
            return x * x * c % mod

result = 0
for _ in range(n):
    a, b = map(int, input().split())
    result += fpow(a, mod-2)*b%mod
    result %= mod
print(result)