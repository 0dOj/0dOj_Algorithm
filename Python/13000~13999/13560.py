n = int(input())
points = list(map(int, input().split()))
ans = 0

if sum(points) == n * (n-1) / 2:
    
    points.sort(reverse=True)
    point = 0

    for i in range(n):
        point += (n - 1 - i)
        point -= points[i]
        
        if point < 0:
            print(-1)
            exit(0)
            
    print(1)
    
else:
    print(-1)