from collections import defaultdict

wordDic = defaultdict(int)
result = 0

for i in range(int(input())):
    chrDic = {}
    arr = []
    word = input()
    num = 0

    for c in word:
        if not c in chrDic:
            chrDic[c] = num
            num += 1
        arr.append(chrDic[c])

    arr = tuple(arr)
    result += wordDic[arr]
    wordDic[arr] += 1

print(result)