import re

color = {'normal': '\x1b[0m',
         'green': '\033[92m',
         'red': '\033[91m',
         'greenbg': '\x1b[6;30;42m',
         }

#RE_ABC = re.compile(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
RE_ABC = re.compile(r'((1\d{2})|(2[0-5]{2})|([1-9]{1,2}))\.((1\d{2})|(2[0-5]{2})|([1-9]{1,2}))\.((1\d{2})|(2[0-5]{2})|([1-9]{1,2}))\.((1\d{2})|(2[0-5]{2})|([1-9]{1,2}))')

tests = '''\
to nie jest python Szkolenie
123
250.23.254.2
10.10.1.12
192.168.1.23
moze jednak jest
129.34
1227.0.0.1
827.0.0.1 oraz 192.168.1.42
jednak TO JUZ NIE
Python to nie jest Szkolenie
'''

for text in tests.splitlines():
    m = RE_ABC.search(text)
    if m:
        result = color['green'] + text + color['normal'] + \
                 ": (" + text[:m.start()] + ")(" + \
                 color['greenbg'] + text[m.start():m.end()] + \
                 color['normal'] + ")(" + text[m.end():] + ")"

    else:
        result = color['red'] + text + color['normal'] + \
                 ": (--)(--)(--)"
    print(result)
