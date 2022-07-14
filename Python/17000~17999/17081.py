from sys import stdin
from collections import deque

input = stdin.readline
TYPE = 'TYPE'
NORMAL = 'NORMAL'
BOSS = 'BOSS'
NAME = 'NAME'
HP = 'HP'
ATT = 'ATT'
DEF = 'DEF'
EXP = 'EXP'
EFFECT = 'EFFECT'

n, m = map(int, input().split())

arr = [list(input().rstrip()) for _ in range(n)]

monster_cnt = 0
box_cnt = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == 'B':
            box_cnt += 1
        elif arr[i][j] == '&':
            monster_cnt += 1
        elif arr[i][j] == 'M':
            monster_cnt += 1
            boss_pos = (i, j)
        elif arr[i][j] == '@':
            start_pos = (i, j)
            arr[i][j] = '.'

order = deque(input().rstrip())

monster_db = {}
for i in range(monster_cnt):
    l = input().split()

    monster_pos = (int(l[0])-1, int(l[1])-1)
    monster_db[monster_pos] = {
        TYPE: BOSS if monster_pos == boss_pos else NORMAL, 
        NAME: l[2],
        ATT: int(l[3]),
        DEF: int(l[4]),
        HP: int(l[5]),
        EXP: int(l[6])
    }

box_db = {}
for i in range(box_cnt):
    l = input().split()

    box_pos = (int(l[0])-1, int(l[1])-1)
    box_db[box_pos] = {
        TYPE: l[2],
        EFFECT: l[3]
    }

pla_LV = 1
pla_remHP = 20
pla_curHP = 20
pla_att = 2
pla_def = 2
pla_curEXP = 0
pla_maxEXP = 5

wea = 0
arm = 0
acc = set()

def gameover(status, killed_by):
    global turn, pla_LV, pla_remHP, pla_curHP, pla_att, wea, pla_def, arm, pla_curEXP, pla_maxEXP, x, y
    if status != 'lose':
        arr[x][y] = '@'
    for i in range(n):
        print(''.join(arr[i]))
    print(f'Passed Turns : {turn}')
    print(f'LV : {pla_LV}')
    print(f'HP : {max(0, pla_remHP)}/{pla_curHP}')
    print(f'ATT : {pla_att}+{wea}')
    print(f'DEF : {pla_def}+{arm}')
    print(f'EXP : {pla_curEXP}/{pla_maxEXP}')
    if status == 'win':
        print('YOU WIN!')
    elif status == 'lose':
        print(f'YOU HAVE BEEN KILLED BY {killed_by}..')
    else:
        print('Press any key to continue.')
    exit(0)

turn = 0
x, y = start_pos
while order:
    turn += 1

    dir = order.popleft()
    if   dir == 'L': y -= 1 if 0 <= y-1 < m and arr[x][y-1] != '#' else 0
    elif dir == 'R': y += 1 if 0 <= y+1 < m and arr[x][y+1] != '#' else 0
    elif dir == 'U': x -= 1 if 0 <= x-1 < n and arr[x-1][y] != '#' else 0
    elif dir == 'D': x += 1 if 0 <= x+1 < n and arr[x+1][y] != '#' else 0

    if arr[x][y] == '.':
        continue

    elif arr[x][y] == '^':
        if 'DX' in acc:
            pla_remHP -= 1
        else:
            pla_remHP -= 5
        if pla_remHP <= 0:
            if 'RE' in acc:
                pla_remHP = pla_curHP
                acc.remove('RE')
                x, y = start_pos
            else:
                gameover('lose', 'SPIKE TRAP')

    elif arr[x][y] == '&' or arr[x][y] == 'M':
        first_attack = True
        first_defence = False
        mon_type = monster_db[(x, y)][TYPE]
        if mon_type == BOSS and 'HU' in acc:
            pla_remHP = pla_curHP
            first_defence = True
        mon_hp = monster_db[(x, y)][HP]
        mon_att = monster_db[(x, y)][ATT]
        mon_def = monster_db[(x, y)][DEF]

        while True:
            if 'CO' in acc and first_attack:
                first_attack = False
                if 'DX' in acc:
                    mon_hp -= max(1, (pla_att+wea)*3 - mon_def)
                else:
                    mon_hp -= max(1, (pla_att+wea)*2 - mon_def)
            else:
                mon_hp -= max(1, pla_att+wea - mon_def)

            if mon_hp <= 0:
                mon_exp = monster_db[(x, y)][EXP]
                pla_curEXP += int(mon_exp*1.2) if 'EX' in acc else mon_exp
                if pla_curEXP >= pla_maxEXP:
                    pla_LV += 1
                    pla_curHP += 5
                    pla_remHP = pla_curHP
                    pla_att += 2
                    pla_def += 2
                    pla_curEXP = 0
                    pla_maxEXP += 5
                elif 'HR' in acc:
                    pla_remHP = min(pla_curHP, pla_remHP+3)

                if mon_type == BOSS:
                    gameover('win', None)

                del monster_db[(x, y)]
                arr[x][y] = '.'
                break

            if first_defence: 
                first_defence = False
                continue
            else:
                pla_remHP -= max(1, mon_att - (pla_def+arm))

            if pla_remHP <= 0:
                if 'RE' in acc:
                    pla_remHP = pla_curHP
                    acc.remove('RE')
                    x, y = start_pos
                    break

                else:
                    gameover('lose', monster_db[(x, y)][NAME])

    elif arr[x][y] == 'B':
        box_type = box_db[(x, y)][TYPE]
        box_effect = box_db[(x, y)][EFFECT]
        if box_type == 'W':
            wea = int(box_effect)
        elif box_type == 'A':
            arm = int(box_effect)
        else:
            if len(acc) != 4:
                acc.add(box_effect)
                
        del box_db[(x, y)]
        arr[x][y] = '.'

gameover('None', None)