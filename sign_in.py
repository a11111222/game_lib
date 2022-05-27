import time as ti

from bag import Bag

# 初始化背包
try:
    with open('resources/bi.txt', 'r') as p:
        a = p.read()
    with open('resources/inside.txt', 'r') as p:
        b = p.read()
    bag = Bag(int(a), list(b))
except FileNotFoundError:
    bag = Bag('0', '')
    with open('resources/bi.txt', 'w') as p:
        p.write(bag.bi)
    with open('resources/inside.txt', 'w') as p:
        p.write(bag.inside)


def sign_in():
    with open('resources/sign_in.txt', 'r') as p:
        a = int(p.read())
    with open('resources/sign_in.txt', 'w') as p:
        p.write(ti.strftime('%d'))
    with open('resources/sign_in.txt', 'r') as p:
        b = int(p.read())
# -------------------------------------有问题----------------------------------------------------------
# if a != b:
# bag.bi = int(bag.bi)
# bag.bi += 10000
# str(bag.bi)
# print('签到完成')
# with open('resources/bi.txt', 'w') as p:
# p.write(str(bag.bi))
# else:
# print('你已经签过到了，请明天再来')
