T = int(input())

for i in range(T):
    txt = input()
    row = 0
    score = 0

    for i in range(len(txt)):
        if txt[i] == "O":
            row += 1
            score += row
        else:
            row = 0

    print(score)