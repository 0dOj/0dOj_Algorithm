from sys import stdin

input = stdin.readline

for _ in range(int(input())):
    n = int(input())
    arr = tuple(map(int, input().split()))

    dic = {}
    for i in range(n):
        dic[i] = arr[i]-1

    visit = [False] * n
    stu_cnt = 0
    for i in range(n):
        if not visit[i]:
            visit[i] = True
            stu_set = {i}
            stu_list = [i]
            x = i
            while True:
                x = dic[x]
                if x in stu_set:
                    stu_cnt += len(stu_list[:stu_list.index(x)])
                    break
                elif not visit[x]:
                    visit[x] = True
                    stu_set.add(x)
                    stu_list.append(x)
                else:
                    stu_cnt += len(stu_list)
                    break

    print(stu_cnt)