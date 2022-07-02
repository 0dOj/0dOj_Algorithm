T = int(input())

for i in range(T):
    
    M, N, K = map(int, input().split()) # 가로길이 M, 세로길이 N, 배추개수 K
    queue = []
    farm = []
    worm = 0
    
    for i in range(K):
        X, Y = map(int, input().split())
        farm.append([X, Y])
        
    while True:
        if queue == []:
            queue.append(farm[0])
            farm.remove(farm[0])
            worm += 1
        
        X = queue[0][0]; Y = queue[0][1]
        if [X-1, Y] in farm:
            queue.append([X-1, Y])
            farm.remove([X-1, Y])
        if [X+1, Y] in farm:
            queue.append([X+1, Y])
            farm.remove([X+1, Y])
        if [X, Y-1] in farm:
            queue.append([X, Y-1])
            farm.remove([X, Y-1])
        if [X, Y+1] in farm:
            queue.append([X, Y+1])
            farm.remove([X, Y+1])
            
        del queue[0]
        
        if farm == []:
            break
            
    print(worm)