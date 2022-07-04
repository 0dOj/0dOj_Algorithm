a, b = map(int, input().split())
m = int(input())
anum = list(map(int, input().split()))
anum.reverse()

a_to_d = 0
for i in range(m):
    a_to_d += anum[i] * (a ** i)

d_to_b = []
while a_to_d//b != 0:
    d_to_b.append(a_to_d % b)
    a_to_d //= b
d_to_b.append(a_to_d)
d_to_b.reverse()

print(*d_to_b)