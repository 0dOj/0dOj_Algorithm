odd = ""
sans = ""

s = ",".join(input())
s = s.split(',')
s.sort()

while not s == []:
    data = s[0]
    if s.count(data) % 2 == 1:
        if odd == "":
            odd = data             
        else:
            print("I'm Sorry Hansoo")
            odd = 'break'
            break
        
    a = s.count(data) // 2
    for i in range(a):
        sans = sans + data
        
    while not s.count(data) == 0:
        s.remove(data)

if not odd == 'break':
    print(sans + odd + sans[::-1])