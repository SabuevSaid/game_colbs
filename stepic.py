color_colbs = {}
value_colbs = {}
n, m = list(map(int, input().split()))
reversed_colbs = [input().split() for _ in range(n)]
colbs = []
for y in range(m):
    colb = []
    for x in range(n):
        colb.append(reversed_colbs[x][y])
    colbs.append(colb)
def touch():
    pass
def is_you_can_go(old_colb, new_colb):
    pass
def go():
    pass
def draw():
    pass
def end():
    pass
for i in colbs:
    print(*i)