import copy
import random
import cv

view = [[0] * 4 for i in range(4)]


def form_view(r: str):
    if r == 'w':
        return [[view[x][i] for x in range(len(view[i]))] for i in range(len(view))]
    if r == 'a':
        return copy.deepcopy(view)
    if r == 's':
        return [[view[x][i] for x in range(len(view[i]) - 1, -1, -1)] for i in range(len(view))]
    return [item[::-1] for item in view]


def to_view(r: str, v):
    if r == 'w':
        return [[v[x][i] for x in range(len(v[i]))] for i in range(len(v))]
    if r == 'a':
        return copy.deepcopy(v)
    if r == 's':
        return [[v[x][i] for x in range(len(v[i]))] for i in range(len(v) - 1, -1, -1)]
    return [item[::-1] for item in v]


def zero_to_end(item):
    return [x for x in item if x] + [0] * item.count(0)


def can_merge(v):
    for x in v:
        item = zero_to_end(x)
        if x != item:
            return True
        for i in range(len(item) - 1):
            if item[i] and item[i] == item[i + 1]:
                return True
    return False


def show_view():
    print('-' * 29)
    for v in view:
        print('|', end='')
        for x in v:
            if x:
                print(' %4d |' % x, end='')
            else:
                print(' ' * 6 + '|', end='')
        print()
        print('-' * 29)
    print()


def add_new_item():
    can_add_row = [i for i in view if 0 in i]
    target_row = can_add_row[random.randint(0, len(can_add_row) - 1)]
    can_add_index = [i for i in range(len(target_row)) if not target_row[i]]
    target_index = can_add_index[random.randint(0, len(can_add_index) - 1)]
    target_row[target_index] = random.randint(1, 2) * 2


def merge(v, r: str):
    for x in v:
        x[:] = zero_to_end(x)
        for i in range(len(x) - 1):
            if x[i] and x[i] == x[i + 1]:
                x[i] = x[i] * 2
                x[i + 1] = 0
        x[:] = zero_to_end(x)
    global view
    view = to_view(r, v)
    add_new_item()
    if not game_over():
        play()


def game_over():
    if can_merge(form_view('w')) or can_merge(form_view('a')) or can_merge(form_view('s')) or can_merge(form_view('d')):
        return False
    show_view()
    print('游戏结束')
    return True


def play():
    show_view()
    # ipt = input()
    ipt = cv.cvview()

    if ipt not in ('w', 'a', 's', 'd'):
        print('输入有误')
        play()
    else:
        v = form_view(ipt)
        if can_merge(v):
            return merge(v, ipt)
        print('操作失败')
        play()


add_new_item()
play()
