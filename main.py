from time import sleep
from bag import Bag
from login import login
import random
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

def view():
    login()
    print('欢迎!\n若想实现功能，请按旁边的对应按键，退出输入a')
    while True:
        print('游戏------------> 1')
        print('更新日志---------> 2')
        a = input()
        if a == '1':
            print('游戏初始化，请稍后')
            while True:
                sleep(random.randint(1,5))
                break
            print('完成.')
            print('--------------------------------------')
        if a == '2':
            print('1.0.0版本 ：更新背包系统\n1.0.1版本 ：更新注册界面\n当前版本 1.0.1')
            print('--------------------------------------')
        if a == 'a':
            break
view()