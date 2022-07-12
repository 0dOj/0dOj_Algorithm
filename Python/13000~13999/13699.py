n = int(input())

t = [1]
for _ in range(n):
    d = 0
    lt = len(t)
    for i in range(lt):
        d += t[i] * t[lt-i-1]
    t.append(d)
print(t[-1])