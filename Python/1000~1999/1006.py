from sys import stdin

input = stdin.readline

def dp(p):
    for i in range(2, n-1+p):
        if arr_up[i-1]+arr_up[i] <= w:
            dp_up[i] = min(dp_both[i-1]+1, dp_down[i-1]+1)
        else:
            dp_up[i] = min(dp_both[i-1]+1, dp_down[i-1]+2)

        if arr_down[i-1]+arr_down[i] <= w:
            dp_down[i] = min(dp_both[i-1]+1, dp_up[i-1]+1)
        else:
            dp_down[i] = min(dp_both[i-1]+1, dp_up[i-1]+2)

        if arr_up[i]+arr_down[i] <= w:
            dp_both[i] = min(dp_both[i-1]+1, dp_up[i]+1, dp_down[i]+1)
        else:
            dp_both[i] = min(dp_both[i-1]+2, dp_up[i]+1, dp_down[i]+1)

        if arr_up[i-1]+arr_up[i] <= w and arr_down[i-1]+arr_down[i] <= w:
            dp_both[i] = min(dp_both[i], dp_both[i-2]+2)

for _ in range(int(input())):
    n, w = map(int, input().split())

    arr_up = tuple(map(int, input().split()))
    arr_down = tuple(map(int, input().split()))

    if n == 1:
        print(1) if w >= arr_up[0] + arr_down[0] else print(2)
    elif n == 2:
        a = 4
        a -= (1 if w >= arr_up[0] + arr_down[0] else 0)
        a -= (1 if w >= arr_up[1] + arr_down[1] else 0)
        b = 4
        b -= (1 if w >= arr_up[0] + arr_up[1] else 0)
        b -= (1 if w >= arr_down[0] + arr_down[1] else 0)
        print(min(a, b))
    elif n >= 3:

        ans = 20000

        dp_up = [2*i+1 for i in range(n)]
        dp_both = [2*(i+1) for i in range(n)]
        dp_down = [2*i+1 for i in range(n)]
        
        if w >= arr_up[0]+arr_up[-1]:
            dp_both[0] = 2
            dp_up[1] = 3
            dp_down[1] = 2 if w >= arr_down[0]+arr_down[1] else 3
            dp_both[1] = 3 if w >= arr_up[1]+arr_down[1] or w >= arr_down[0]+arr_down[1] else 4

            dp(0)

            dp_down[-1] = min(dp_up[-2] + (1 if w >= arr_down[-1] + arr_down[-2] else 2), dp_both[-2] + 1)

            ans = min(ans, dp_down[-1])

            dp_up = [2*i+1 for i in range(n)]
            dp_both = [2*(i+1) for i in range(n)]
            dp_down = [2*i+1 for i in range(n)]

        if w >= arr_down[0]+arr_down[-1]:
            dp_both[0] = 2
            dp_down[1] = 3
            dp_up[1] = 2 if w >= arr_up[0]+arr_up[1] else 3
            dp_both[1] = 3 if w >= arr_down[1]+arr_up[1] or w >= arr_up[0]+arr_up[1] else 4

            dp(0)

            dp_up[-1] = min(dp_down[-2] + (1 if w >= arr_up[-1] + arr_up[-2] else 2), dp_both[-2]+1)

            ans = min(ans, dp_up[-1])

            dp_up = [2*i+1 for i in range(n)]
            dp_both = [2*(i+1) for i in range(n)]
            dp_down = [2*i+1 for i in range(n)]

        if w >= arr_down[0]+arr_down[-1] and w >= arr_up[0]+arr_up[-1]:
            dp_both[0] = 2
            dp_up[1] = 3
            dp_down[1] = 3
            dp_both[1] = 3 if w >= arr_down[1]+arr_up[1] else 4

            dp(0)

            ans = min(ans, dp_both[-2])

            dp_up = [2*i+1 for i in range(n)]
            dp_both = [2*(i+1) for i in range(n)]
            dp_down = [2*i+1 for i in range(n)]

        dp_both[0] = 1 if w >= arr_up[0]+arr_down[0] else 2
        dp_up[1] = min(2 if w >= arr_up[0]+arr_up[1] else 3, dp_both[0]+1)
        dp_down[1] = min(2 if w >= arr_down[0]+arr_down[1] else 3, dp_both[0]+1)
        dp_both[1] = min(dp_both[0] + (1 if w >= arr_up[1]+arr_down[1] else 2), 2 if (w >= arr_up[0]+arr_up[1] and w >= arr_down[0]+arr_down[1]) else 4, dp_up[1]+1, dp_down[1]+1)

        dp(1)
        
        ans = min(ans, dp_both[-1])

        print(ans)