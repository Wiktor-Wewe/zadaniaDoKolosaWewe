"""
znajdz indeks elementu '5'  w tablicy [5,101,"0x5",'7','0o5','5', 4,6,'python>c']
"""

t = [5,101,"0x5",'7','0o5','5', 4,6,'python<c']

for x in range(len(t)):
    if t[x] == '5':
        print(x)
        break
