txt = input()
ans = ""
for i in range(97, 123):
    for j in range(len(txt)):
        find = False
        if txt[j] == chr(i):
            ans += str(j) + " "
            find = True
            break
    if find == False:
        ans += "-1 "

print(ans)
