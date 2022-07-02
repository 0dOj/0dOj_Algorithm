n = int(input())
arr = list(map(int, input().split()))

def DP():
    lst = []
    for i in range(n):
        mx = 1
        for j in range(i):
            if arr[j] < arr[i]:
                mx = max(mx, lst[j]+1)
        lst.append(mx)

    return lst

ldp = DP()

arr.reverse()

rdp = DP(); rdp.reverse()

mx = 1
for i in range(n):
    mx = max(mx, ldp[i]+rdp[i]-1)

print(mx)