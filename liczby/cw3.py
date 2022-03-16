"""
napisz program który wypisze wielokrotności liczby n mniejsze od liczby m, podzielne przez k
"""

def f(n, m, k):
    i=1
    while(n*i<m):
        if n*i%k==0:
            print(n*i)
        i+=1
f(2, 400, 4)
