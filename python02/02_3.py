def frange(od, do, krok=0.1):
    while True:
        if od + krok > do:
            break
        else:
            yield od
            #print(self.od)
            od += krok
    raise StopIteration


it = frange(0.1, 2.9, 0.4)

for x in it:
    print(x)
