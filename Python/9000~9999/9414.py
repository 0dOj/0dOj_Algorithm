from sys import stdin

input = stdin.readline

for _ in range(int(input())):
    arr = []
    while True:
        x = int(input())
        if not x:
            break
        else:
            arr.append(x)
    arr.sort()

    ans = 0
    i = 1
    while arr:
        x = arr.pop()
        ans += 2 * (x ** i)
        i += 1
    if ans <= 5000000:
        print(ans)
    else:
        print("Too expensive")