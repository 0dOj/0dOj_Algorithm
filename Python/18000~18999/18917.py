from sys import stdin
input = stdin.readline

sm = 0; xor = 0
for i in range(int(input())):
    query = tuple(map(int, input().split()))
    if query[0] == 3:
        print(sm)
    elif query[0] == 4:
        print(xor)
    elif query[0] == 1:
        sm += query[1]
        xor ^= query[1]
    elif query[0] == 2:
        sm -= query[1]
        xor ^= query[1]