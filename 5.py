def get_char(od, do, krok=1):
    list = []
    for x in range(od, do + 1, krok):
        list.append(chr(x))
    return list

print(get_char(114, 120))
print(get_char(114, 120, 3))