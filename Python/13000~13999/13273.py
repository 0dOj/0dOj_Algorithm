roma = {'M':1000, 'CM':900, 'D':500, 'CD':400, 'C':100, 'XC':90,
        'L':50, 'XL':40, 'X':10, 'IX': 9, 'V':5, 'IV': 4, 'I':1}

T = int(input())

for i in range(T):

    num = input()

    if num.isdigit() == True:

        anum = int(num)
        rnum = ""
        j = 0

        while anum != 0:
            while anum >= list(roma.values())[j]:
                rnum += list(roma.keys())[j]
                anum -= list(roma.values())[j]
            j += 1

        print(rnum)

    else:
        
        lst = list(num)
        lst.reverse()
        lstsum = 0
        data = 0

        for i in lst:
            if roma[i] >= data:
                lstsum += roma[i]
                data = roma[i]
            else:
                lstsum -= roma[i]

        print(lstsum)