N = int(input())
i = 0
while True:
    s = str(i)
    cnt = i
    for j in range(len(s)):
        cnt += int(s[j])
    if N == cnt:
        print(i)
        break
    elif N < i:
        print("0")
        break
    else:
        i += 1