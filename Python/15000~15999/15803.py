arr = sorted([tuple(map(int, input().split())) for _ in range(3)])

x = 0
y = 1

if (arr[2][x] - arr[0][x]) * (arr[1][y] - arr[0][y]) == (arr[1][x] - arr[0][x]) * (arr[2][y] - arr[0][y]):
    print('WHERE IS MY CHICKEN?')
else:
    print('WINNER WINNER CHICKEN DINNER!')