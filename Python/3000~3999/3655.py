for T in range(int(input())):
    n = int(input())
    arr = input()

    dic = {}

    for i in range(n):
        c = arr[i]
        if not c in dic:
            dic[c] = [i, 1]
        else:
            dic[c][0] = i
            dic[c][1] += 1

    new_arr = sorted(dic.values())

    cnt = 0
    new_idx = -1

    for ori_idx, num in new_arr:
        new_idx += num
        cnt += (ori_idx-new_idx)*num*5

    print(cnt)