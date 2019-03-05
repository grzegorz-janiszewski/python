import random

def myiter():
    num = random.random()
    if num < 0.1:
        #print("%.5s" % self.num)
        raise StopIteration
    new = random.random()
    while abs(new - num) < 0.4:
        #print("%.5s" % new)
        print("*", end='')
        new = random.random()
    num = new
    yield new

a = myiter()

for x in a:
    print(x)