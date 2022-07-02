T = int(input())

for i in range(T):
    N = int(input())
    data1 = 1
    data2 = 1
    if N == 0:
        print("1 0")
    elif N == 1:
        print("0 1")
    else:
        if N % 2 == 1:
            data2 += data1
        for i in range((N-2) // 2):
            data1 += data2
            data2 += data1
        print(data1, data2)