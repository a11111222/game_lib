from bag import Bag

# 初始化背包
try:
    with open('bi.txt', 'r') as p:
        a = p.read()
    with open('inside.txt', 'r') as p:
        b = p.read()
    bag = Bag(int(a), list(b))
except FileNotFoundError:
    bag = Bag('0', '')
    with open('bi.txt', 'w') as p:
        p.write(bag.bi)
    with open('inside.txt', 'w') as p:
        p.write(bag.inside)
# 克隆bag
b = bag.inside[:]
bag1 = Bag(a, b)
# 完成转化
for a in b[:]:
    if a == 'a':
        bag1.inside.remove(a)
        bag1.inside.append('生命药水')
if __name__ == '__main__':
    bag1.view()
