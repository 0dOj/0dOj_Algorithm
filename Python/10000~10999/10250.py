import sys
input = sys.stdin.readline

T = int(input())

for i in range(T):
    H, W, N = map(int, input().split())

    f = N % H
    r = N // H + 1
    if f == 0: f = H; r -= 1
    if r < 10: r = "0" + str(r)
    print(str(f) + str(r))