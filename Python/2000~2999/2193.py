n = int(input())

dp_0 = [0]
dp_1 = [1]

for i in range(n-1):
    dp_0.append(dp_0[i] + dp_1[i])
    dp_1.append(dp_0[i])

print(dp_0[-1]+dp_1[-1])