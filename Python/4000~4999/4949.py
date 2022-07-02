while True:
    txt = input()
    if txt == ".":
        break
    stack = []; bal = "yes"
    for i in txt:
        if i == '(':
            stack.append('(')
        elif i == '[':
            stack.append('[')
        elif i == ')':
            if stack:
                if stack.pop() != '(':
                    bal = "no"
                    break
            else:
                bal = "no"
                break
        elif i == ']':
            if stack:
                if stack.pop() != '[':
                    bal = "no"
                    break
            else:
                bal = "no"
                break
    if stack:
        bal = "no"
    print(bal)