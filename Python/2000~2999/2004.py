n, m = map(int, input().split())
n2 = n-m; n3 = m

def fcnt(n, k):
    cnt = 0
    while n:
        n //= k
        cnt += n
    return cnt

print(min(fcnt(n, 5)-fcnt(n2, 5)-fcnt(n3, 5), fcnt(n, 2)-fcnt(n2, 2)-fcnt(n3, 2)))