escape = False
list = []

print("Podawaj lancuchy znakow, zakonczenie wprowadzania pustym wierszem:")
while not escape:
    x = input()
    if x != '':
        list.append(x)
    else:
        escape = True

print(list)

maxlen = 0
for x in list:
    if len(x) > maxlen: maxlen = len(x)

print('max len = ', maxlen)

header = ''
count = 0
for x in range(0,maxlen):
    count += 1
    if count == 10:
        count = 0
        header += "0"
    else:
        header += str(count)


print(header)
for x in list:
    form = '{:>' + str(maxlen) + '}'
    print(form.format(x))