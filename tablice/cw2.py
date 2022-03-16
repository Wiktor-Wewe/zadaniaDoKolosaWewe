"""
zamień element pierwszy i ostatni w tablicy [1,2,3, 'wiadomo']
"""

t = [1,2,3, 'wiadomo']
buff = t[0]
t[0] = t[-1]
t[-1] = buff
print(t)
