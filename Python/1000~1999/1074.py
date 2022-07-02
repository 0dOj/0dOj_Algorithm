n, r, c = map(int, input().split())
cnt = 0

def Z(n, r, c):
    global cnt
    if n == 0:
        return
    if r >= 2**(n-1):
        cnt += 2**(2*n-1)
    if c >= 2**(n-1):
        cnt += 2**(2*n-2)
    Z(n-1, r%(2**(n-1)), c%(2**(n-1)))

Z(n, r, c)
print(cnt)