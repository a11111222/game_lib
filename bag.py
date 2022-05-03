class Bag:
    def __init__(self, bi, inside):
        self.bi = bi
        self.inside = inside

    def view(self):
        if self.inside == '[]' or not self.inside:
            print('你没有东西！')
        else:
            print('东西：')
            a = 1
            for big1 in self.inside:
                a += 1
                print(f'第{a}个:{big1}')

