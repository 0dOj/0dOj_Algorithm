import sys
input = sys.stdin.readline

N, M, B = map(int, input().split())
land = []
timeAns = 128000000

for i in range(N):
    lst = list(map(int, input().split()))
    land += lst

for height in range(0, 257):
    block = B
    time = 0
    for i in range(len(land)):
        sub = land[i] - height
        if sub > 0: # height 보다 땅이 더 높으면
            time += sub * 2
            block += sub
        elif sub < 0: # height 보다 땅이 더 낮으면
            time += abs(sub)
            block -= abs(sub)
    if block >= 0: # block이 0보다 클때만 기록
        if time <= timeAns:
            timeAns = time
            heightAns = height

print(timeAns, heightAns)