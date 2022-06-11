import matplotlib.pyplot as  plt
import numpy as np
import pandas as pd

data = pd.read_excel('ceny2.xlsx')
print(data.groupby(['Rodzaje towarów'])['Wartość'].mean())

lata = data.Rok.unique()
nazwy = data['Rodzaje towarów'].unique()
ryz_wartosci = data[data['Rodzaje towarów'] == nazwy[0]]['Wartość']
maka_wartosci = data[data['Rodzaje towarów'] == nazwy[1]]['Wartość']

plt.plot(lata, ryz_wartosci, label = 'Ryż', color = 'violet')
plt.plot(lata, maka_wartosci, label = 'Mąka', color = 'navy')
plt.title('Zmiana cen produktów na przestrzeni lat')
plt.xlabel('Lata')
plt.ylabel('Cena w zł/kg')

plt.annotate('21376969', xy=(2010,2))
plt.legend()

plt.savefig('zad2.jpg')
