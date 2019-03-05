import random


class MyIter:
    def __init__(self):
        self.num = 2

    def __iter__(self):
        return self

    def __next__(self):
        if self.num < 0.1:
            #print("%.5s" % self.num)
            raise StopIteration
        new = random.random()
        while abs(new - self.num) < 0.4:
            #print("%.5s" % new)
            print("*", end='')
            new = random.random()
        self.num = new
        return new

a = MyIter()

for x in a:
    print(x)
