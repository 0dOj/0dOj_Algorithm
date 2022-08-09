dir = {'U': (0, -6), 'D': (0, 6), 'L': (-6, 0), 'R': (6, 0), 'DL': (-5, 5), 'DR': (5, 5)}

upp = set(['A', 'B', 'C', 'D'])
low = set(['a', 'b', 'c', 'd'])

piece = {}
dis_set = set()
def init_pos(p):
    piece[p] = {'pos': [30, 30], 'dir': dir['U']}
    dis_set.add(p)
for p in upp|low:
    init_pos(p)

n = int(input())
for _ in range(n):

    move = input().split()

    p = move[0]

    cnt = move[1].count('F')
    if cnt == 0: cnt = 5

    move_with = set([p])

    if p in upp:
        st = upp
    else:
        st = low
    for i in st:
        if not i in dis_set and piece[p]['pos'] == piece[i]['pos']:
            move_with.add(i)

    for i in move_with:
        p_cnt = cnt
        if i in dis_set:
            dis_set.remove(i)

        while p_cnt:
            piece[i]['pos'][0] += piece[i]['dir'][0]
            piece[i]['pos'][1] += piece[i]['dir'][1]

            if piece[i]['pos'] == [30, 0]:
                piece[i]['dir'] = dir['L']

            elif piece[i]['pos'] == [0, 0]:
                piece[i]['dir'] = dir['D']

            elif piece[i]['pos'] == [0, 30] or piece[i]['pos'] == [30, 30]:
                piece[i]['dir'] = dir['R']

            elif piece[i]['pos'] == [36, 30]:
                dis_set.add(i)
                break

            p_cnt -= 1

        if piece[i]['pos'] == [30, 0]:
            piece[i]['dir'] = dir['DL']

        elif piece[i]['pos'] == [0, 0] or piece[i]['pos'] == [15, 15]:
            piece[i]['dir'] = dir['DR']

    if st == upp: st = low
    elif st == low: st = upp

    for i in st:
        if not i in dis_set and piece[p]['pos'] == piece[i]['pos']:
            init_pos(i)

board = '''..----..----..----..----..----..
..    ..    ..    ..    ..    ..
| \                          / |
|  \                        /  |
|   \                      /   |
|    ..                  ..    |
..   ..                  ..   ..
..     \                /     ..
|       \              /       |
|        \            /        |
|         ..        ..         |
|         ..        ..         |
..          \      /          ..
..           \    /           ..
|             \  /             |
|              ..              |
|              ..              |
|             /  \             |
..           /    \           ..
..          /      \          ..
|         ..        ..         |
|         ..        ..         |
|        /            \        |
|       /              \       |
..     /                \     ..
..   ..                  ..   ..
|    ..                  ..    |
|   /                      \   |
|  /                        \  |
| /                          \ |
..    ..    ..    ..    ..    ..
..----..----..----..----..----..'''
board_list = board.split('\n')

for i in (upp|low)-dis_set:
    x = piece[i]['pos'][0]
    y = piece[i]['pos'][1]

    if i.upper() == 'B':
        x += 1
    elif i.upper() == 'C':
        y += 1
    elif i.upper() == 'D':
        x += 1; y += 1

    board_list[y] = board_list[y][:x] + i + board_list[y][x+1:]

for line in board_list:
    print(line)