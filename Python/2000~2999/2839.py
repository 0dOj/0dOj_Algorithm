N = int(input())

if N == 7 or N == 4 or N == 2 or N ==1:
    print("-1")
else:
    if N % 5 == 0:
        print(N // 5)
    elif N % 5 == 4 or N % 5 == 2:
        print(N // 5 + 2)
    elif N % 5 == 3 or N % 5 == 1:
        print(N // 5 + 1)