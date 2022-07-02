n, k = map(int, input().split())
cnt = 0; set1 = {n}

visit = [[False, False] for i in range(500001)]; visit[n][0] = True # 0이 짝수, 1이 홀수

while True:

    if visit[k][cnt%2] == True:
        print(cnt)
        exit(0)
    
    set2 = set1; set1 = set([])
    cnt += 1
    k += cnt

    if k > 500000: 
        print(-1)
        exit(0)

    for x in set2:
        for i in (x-1, x+1, x*2):
            if i == k: 
                print(cnt)
                exit(0)
            if 0 <= i <= 500000 and visit[i][cnt%2] == False:
                visit[i][cnt%2] = True
                set1.add(i)