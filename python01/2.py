def above_average(lista):
    aver = 0
    sum = 0

    for x in lista:
        sum += x
    aver = sum  / len(lista)

    res2 = [x for x in lista if x > aver]
    return res2

print(above_average(range(1,10)))
