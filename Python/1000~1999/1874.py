n = int(input())
stack = []
cnt = 0
ans = []
no = False

for i in range(n):
    data = int(input())
    if no == False:
        while data > cnt:
            cnt += 1
            stack.append(cnt)
            ans.append('+')
        if stack.pop() == data:
            ans.append('-')
        else:
            no = True

if no == True:
    print("NO")
else:
    for i in range(len(ans)):
        print(ans[i])