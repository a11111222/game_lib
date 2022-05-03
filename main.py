from bag import Bag
try:
    with open('bi.txt','r') as p:
        a = p.read()
    with open('inside.txt','r') as p:
        b = p.read()
    bag = Bag(int(a),list(b))
except FileNotFoundError:
    bag = Bag('0','')
    with open('bi.txt','w') as p:
        p.write(bag.bi)
    with open('inside.txt','w') as p:
        p.write(bag.inside)

if __name__ == '__main__':
    bag.view()