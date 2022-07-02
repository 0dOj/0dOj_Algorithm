import heapq
from collections import defaultdict
from sys import stdin
input = stdin.readline


for i in range(int(input())):
    maxheap = []; minheap = []; maxabd = defaultdict(int,{}); minabd = defaultdict(int,{})
    for i in range(int(input())):
        order = input().split(); x = int(order[1])
        if order[0] == "I":
            heapq.heappush(maxheap, -x)
            heapq.heappush(minheap, x)
        if order[0] == "D":
            if x == 1:
                try:
                    mx = -heapq.heappop(maxheap)
                    while minabd[mx] > 0:
                        minabd[mx] -= 1
                        mx = -heapq.heappop(maxheap)
                    maxabd[mx] += 1
                except:
                    maxheap = []; minheap = []; maxabd = defaultdict(int,{}); minabd = defaultdict(int,{})
            elif x == -1:
                try:
                    mn = heapq.heappop(minheap)
                    while maxabd[mn] > 0:
                        maxabd[mn] -= 1
                        mn = heapq.heappop(minheap)
                    minabd[mn] += 1
                except:
                    maxheap = []; minheap = []; maxabd = defaultdict(int,{}); minabd = defaultdict(int,{})
    for i in range(len(maxheap)): maxheap[i] *= -1
    its = set(maxheap) & set(minheap)
    if its:
        print(max(list(its)), min(list(its)))
    else:
        print("EMPTY")