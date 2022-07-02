import sys
input = sys.stdin.readline

N = int(input())
i = 1
room = 1

if N == 1:
    print(1)
else:
    while not room < N <= room + 6 * i:
        room += 6 * i
        i += 1

    print(i + 1)