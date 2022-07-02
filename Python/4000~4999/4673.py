visit = [False] * 10001
for i in range(1, 10001):
    if visit[i] == False:
        print(i)
        t = i
        while t <= 10000:
            visit[t] = True
            l = list(map(int, list(str(t))))
            t += sum(l)