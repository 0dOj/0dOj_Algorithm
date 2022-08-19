num = input()
cnt = [0] * 10

for k in range(len(num)):
    idx = len(num)-1-k

    for i in range(10):
        cnt[i] += int(num[:idx] if num[:idx] else 0)*(10**k)
    cnt[0] -= 10**k

    for i in range(int(num[idx])):
        cnt[i] += 10**k
    cnt[int(num[idx])] += int(num[idx+1:] if num[idx+1:] else 0)+1

print(*cnt)