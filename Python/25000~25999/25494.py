for T in range(int(input())):
    x, y, z = map(int, input().split())

    cnt = 0

    for a in range(1, x+1):
        for b in range(1, y+1):
            for c in range(1, z+1):
                if a%b == b%c == c%a:
                    cnt += 1

    print(cnt)