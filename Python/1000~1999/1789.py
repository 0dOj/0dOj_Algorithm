s = int(input())
i = 0
sigma = 0

while s >= sigma:
    i += 1
    sigma = i * (i + 1) // 2

print(i-1)