"""
zadeklaruj liste za pomocą list comprehension
"""

from random import randint
t = [randint(0, 20) for _ in range(0, randint(4, 23))]
print(t)
