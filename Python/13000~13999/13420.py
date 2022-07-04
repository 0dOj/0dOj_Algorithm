for _ in range(int(input())):
    line = input().split()
    if eval(line[0]+line[1]+line[2]) == int(line[4]):
        print("correct")
    else:
        print("wrong answer")