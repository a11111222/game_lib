from bag import Bag
from login import login
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
# 克隆bag
b = bag.inside[:]
bag1 = Bag(a, b)
# 完成转化
for a in b[:]:
    if a == 'a':
        bag1.inside.remove(a)
        bag1.inside.append('生命药水')
    if a == 'b':
        bag1.inside.remove('b')
        bag1.inside.append('力量药水')
    if a == 'c':
        bag1.inside.remove('c')
        bag1.inside.append('体力丸')
    if a == 'd':
        bag1.inside.remove('d')
        bag1.inside.append('炼金丸')
#注册
login()
#背包
bag1.view()