a, b = input().split(); a = '0' if a == '0' else str(int(a)-1)

def hab(num):
    cnt = [0] * 10

    for k in range(len(num)):
        idx = len(num)-1-k

        for i in range(10):
            cnt[i] += int(num[:idx] if num[:idx] else 0)*(10**k)
        cnt[0] -= 10**k

        for i in range(int(num[idx])):
            cnt[i] += 10**k
        cnt[int(num[idx])] += int(num[idx+1:] if num[idx+1:] else 0)+1

    return sum([i*cnt[i] for i in range(10)])

print(hab(b)-hab(a))