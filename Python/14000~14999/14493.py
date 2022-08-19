from sys import stdin

input = stdin.readline

time = 0
for _ in range(int(input())):
    a, b = map(int, input().split())
    time += 1 if time%(a+b) >= b else b-time%(a+b)+1

print(time)