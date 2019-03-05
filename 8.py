class Liczba:
    def __init__(self, liczba):
        self.liczba = []
        for x in liczba:
            self.liczba.insert(0, x)
    def wyswietl(self):
        return self.liczba
    def __int__(self):
        liczba = 0
        for x in range(0, len(self.liczba)):
            liczba += int(self.liczba[x]) * ( 10**x )
        return liczba
    def __mul__(self, other):
        return self.__int__() * other
    def silnia(self):
        res = 1
        for x in range(1, self.__int__() + 1):
            res *= x
        return res

a = Liczba('45')
print(a.wyswietl())
print(int(a))

print(a * 10)
print(a * 23)

print(a.silnia())

