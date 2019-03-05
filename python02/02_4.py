from random import randrange

class RandRunner:
    def __init__(self, lista):
        self.lista = lista

    def __iter__(self):
        return self

    def __next__(self):
        if self.lista:
            element = randrange(len(self.lista))
            return self.lista.pop(element)
        else:
            raise StopIteration


for x in RandRunner([1, 2, 3, 4, 5]):
    print(x)