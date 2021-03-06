import re

color = {'normal': '\x1b[0m',
         'green': '\033[92m',
         'red': '\033[91m',
         'greenbg': '\x1b[6;30;42m',
         }

RE_ABC = re.compile(r'python|Python')

tests = '''\
to nie jest python
a to juz jest
a to znowu nie jest Python
moze jednak jest
ale przeciez to jednak python jest
python
Python to nie jest
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
