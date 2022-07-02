txt = input().upper()
dic = {}

for i in range(len(txt)):
    if txt[i] in dic:
        dic[txt[i]] += 1
    else:
        dic[txt[i]] = 1

val = list(dic.values())

if val.count(max(val)) != 1:
    print("?")
else:
    vk = {v:k for k,v in dic.items()}
    print(vk.get(max(dic.values())))