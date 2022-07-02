e, s, m = map(int, input().split())

year = 1
ec = 1
sc = 1
mc = 1
while True:
    if e == ec and s == sc and m == mc:
        print(year)
        exit(0)

    ec += 1
    if ec > 15: ec = 1

    sc += 1
    if sc > 28: sc = 1

    mc += 1
    if mc > 19: mc = 1

    year += 1