from multiprocessing import Process
import time
import random
import concurrent.futures
from multiprocessing import Process

def tabliczka(n, liczba):
    wynik = ""
    for x in range(liczba):
        wynik += ("%5s" % ((x+1)*n))
    time.sleep(random.randint(1,10))
    print(wynik)

rozmiar = int(input("Podaj rozmiar tabliczki:"))

czas = time.time()
tabliczki = [ Process(target=tabliczka, args=(n, rozmiar)) for n in range(1, rozmiar+1) ]

for n in tabliczki:
    n.start()

for n in tabliczki:
    n.join()

print("Czas:", time.time() - czas)
