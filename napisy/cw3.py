"""
napisz program, który ze wzoru na funkcje wybierze współczynnik stojący przy a
"""

def f(n):
    n.replace("y=", "")
    chuj = n.split("x^2")
    return chuj[0]

print(f("y=12x^2"))
