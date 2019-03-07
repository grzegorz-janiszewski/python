from multiprocessing import Process
import time
import random
import concurrent.futures


def tabliczka(n, liczba):
    wynik = ""
    for x in range(liczba):
        wynik += ("%5s" % ((x+1)*n))
    time.sleep(random.randint(1,10))
    return wynik

rozmiar = int(input("Podaj rozmiar tabliczki:"))

czas = time.time()
with concurrent.futures.ThreadPoolExecutor(max_workers=(rozmiar//4)) as executor:
    futs = [ executor.submit(tabliczka, n, rozmiar) for n in range(1,rozmiar+1) ]
    for fut in concurrent.futures.as_completed(futs):
        print(fut.result())
print("Czas:", time.time() - czas)
