class Prostokat:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def pole(self):
        return self.x * self.y
    def obwod(self):
        return self.x * 2 + self.y * 2
    def __add__(self, other):
        return self.pole() + other.pole()

class Kwardat(Prostokat):
    def __init__(self, x):
        self.x = x
        self.y = x

a1 = Prostokat(10, 20)
a2 = Prostokat(5, 2)
a3 = Kwardat(10)

print(a1.pole())
print(a1.obwod())

print(a2.pole())
print(a2.obwod())

print(a3.pole())
print(a3.obwod())

print(a1 + a2)

