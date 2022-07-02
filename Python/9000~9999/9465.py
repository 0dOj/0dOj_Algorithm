for _ in range(int(input())):

    n = int(input())

    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))

    if n == 1:
        print(max(arr1[0], arr2[0]))

    else:
        dp1 = [arr1[0], arr2[0]+arr1[1]]
        dp2 = [arr2[0], arr1[0]+arr2[1]]

        for i in range(2, n):
            dp1.append(max(dp2[i-1], dp2[i-2])+arr1[i])
            dp2.append(max(dp1[i-2], dp1[i-1])+arr2[i])

        print(max(dp1[-1], dp2[-1]))