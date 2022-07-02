n, m = map(int, input().split()); c = 1
for i in range(1, m+1):
    c *= n-i+1
    c //= i
print(c)
