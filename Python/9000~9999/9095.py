for i in range(int(input())):
    n = int(input()); cnt = 0; table = []

    def sum123(n):
        if sum(table) == n:
            global cnt
            cnt += 1
            return
        elif sum(table) > n:
            return
        for i in range(1, 4):
            table.append(i)
            sum123(n)
            table.pop()

    sum123(n)
    print(cnt)