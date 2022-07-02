while True:
    txt = input()
    if txt == "0":
        break
    front = txt[0:len(txt) // 2]
    back = txt[(len(txt) + 1) // 2:]
    
    back = back[::-1]

    if front == back:
        print("yes")
    else:
        print("no")