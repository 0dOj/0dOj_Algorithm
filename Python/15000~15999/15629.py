dic = {'namibia':140, 'kenya':50, 'south-africa':0, 'botswana':0, 'zimbabwe':30, 'zambia':50, 'tanzania':50, 'ethiopia':50}
# 남아공 입국 후 나미비아 -> 나미비아: 40
# 잠비아-짐바브웨 or 짐바브웨-잠비아: 50

southAfrica = False
zimbabwe = False
zambia = False
money = 0

for i in range(int(input())):
    nation = input()
    if nation == 'south-africa':
        southAfrica = True
    if nation == 'namibia' and southAfrica == True:
        dic['namibia'] = 40
    if nation == 'zambia':
        zambia = True
        if zimbabwe == True:
            dic['zambia'] = 20
    elif nation == 'zimbabwe':
        zimbabwe = True
        if zambia == True:
            dic['zimbabwe'] = 0
    else:
        zambia = False; zimbabwe = False
    money += dic[nation]
print(money)