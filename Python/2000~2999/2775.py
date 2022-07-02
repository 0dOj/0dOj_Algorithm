import sys
input = sys.stdin.readline

T = int(input())

for i in range(T):
    k = int(input()); n = int(input())
    ans = 1

    for i in range(k + 1):
        ans = ans * n // (i + 1)
        n += 1

    print(ans)