a, b, v = map(int, input().split())
day = 1

v -= a
day += v // (a-b) + min(1, v % (a-b))
print(day)