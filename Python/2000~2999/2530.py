A, B, C = map(int, input().split())
D = int(input())

while D >= 3600:
    A += 1
    D -= 3600
while D >= 60:
    B += 1
    D -= 60
while D != 0:
    C += 1
    D -= 1
while C >= 60:
    B += 1
    C -= 60
while B >= 60:
    A += 1
    B -= 60
while A >= 24:
    A -= 24
    
print(A, B, C)