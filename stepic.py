import algorithm as al


n, m = list(map(int, input().split()))


def get_colbs():
    reversed_colbs = [list(map(int, input().split())) for _ in range(n)]
    colbs = []
    for y in range(m):
        colb = []
        for x in range(n):
            colb.append(reversed_colbs[x][y])
        colbs.append(colb)
    return colbs
def get_value_colors_in_colbs():
    value_colors_in_colbs = []
    for colb in get_colbs():
        value_colors_in_colb = []
        same_colors = 1
        for color_index in range(len(colb)):
            if colb[color_index] == 0:
                continue
            try:
                if colb[color_index] == colb[color_index + 1]:
                    same_colors += 1
                else:
                    value_colors_in_colb.append([colb[color_index], same_colors])
                    same_colors = 1
            except IndexError:
                value_colors_in_colb.append([colb[color_index], same_colors])
        value_colors_in_colbs.append(value_colors_in_colb)
    return value_colors_in_colbs
def touch():
    pass
def is_you_can_go():
    pass
def go():
    pass
def draw():
    pass
def end():
    completed_colbs = 0
    for colb in get_value_colors_in_colbs():
        if len(set([i[0] for i in colb])) == n:
            completed_colbs += 1
    if completed_colbs == m:
        return True
    else:
        return False