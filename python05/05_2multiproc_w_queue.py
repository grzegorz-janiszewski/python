import time
import random
from multiprocessing import Process, Queue

def tabliczka(n, liczba, q):
    wynik = ""
    for x in range(liczba):
        wynik += ("%5s" % ((x+1)*n))
    time.sleep(random.randint(1,10))
    q.put(wynik)


if __name__ == "__main__":
    rozmiar = int(input("Podaj rozmiar tabliczki:"))

    czas = time.time()
    q = Queue()

    tabliczki = [ Process(target=tabliczka, args=(n, rozmiar, q)) for n in range(1, rozmiar+1) ]

    for n in tabliczki:
        n.start()


    while True:
        print(q.get())
        czas2 = time.time()
        while q.empty():
            print('Kolejka pusta od {:.6f} sekund...'.format(time.time() - czas2))
            time.sleep(2)
            if time.time() - czas2 > 5:
                break
        if time.time() - czas2 > 5:
            break

    for n in tabliczki:
        n.join()

    print("Calkowity czas:", "{:.2f}".format( time.time() - czas))
