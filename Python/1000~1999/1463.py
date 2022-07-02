N = int(input())
lst = [N] * (N + 1); lst[N] = 0

for i in range(N, 0, -1):
    if i % 3 == 0:
        lst[i//3] = min(lst[i//3], lst[i] + 1)

    if i % 2 == 0:
        lst[i//2] = min(lst[i//2], lst[i] + 1)
            
    lst[i-1] = min(lst[i-1], lst[i] + 1)

print(lst[1])