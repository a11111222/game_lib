import random
from time import sleep, strftime
from tqdm import tqdm
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
ship = '--------------------------------------'


def sign_in():
    """签到模块"""
    with open('resources/sign_in.txt', 'r') as p:
        a = int(p.read())
    with open('resources/sign_in.txt', 'w') as p:
        p.write(strftime('%d'))
    with open('resources/sign_in.txt', 'r') as p:
        b = int(p.read())
    if a != b:
        bag.bi = int(bag.bi)
        bag.bi += 10000
        bag.bi = str(bag.bi)
        print('签到完成')
        with open('resources/bi.txt', 'w') as p:
            p.write(bag.bi)
    else:
        print('你已经签过到了，请明天再来')


login()
print('\n欢迎!')
while a != 'b':
    print('\n若想实现功能，请按旁边的对应按键，退出输入b')
    print('游戏------------> 1')
    print('更新日志---------> 2')
    a = input()
    if a == '1':
        print('游戏初始化，请稍后')
        max = random.randint(50, 200)
        for i in tqdm(range(max)):
            sleep(random.uniform(0.05,0.3))
        print('\n完成.')
        while True:
            print('若想实现功能，请按旁边的对应按键，退出输入a\n背包---------> 1')
            print('签到---------> 2')
            a = input()
            if a == '1':
                bag1.view()
                print(f'{ship}\n\n')
            if a == 'a':
                print(ship)
                break
            if a == '2':
                sign_in()
                print(ship)

    if a == '2':
        print('1.0.0版本 ：更新背包系统\n\n'
              '1.0.1版本 ：更新注册界面\n\n'
              '1.0.2版本：优化界面\n'
              '修复返回时退出程序的bug\n\n'
              '1.0.3版本：新增签到\n\n'
              '当前版本 1.0.3')
        print(ship)
