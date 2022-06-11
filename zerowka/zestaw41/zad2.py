import matplotlib.pyplot as  plt
import numpy as np
import pandas as pd

df = pd.read_excel("ceny41.xlsx")
marchew = df[df['Rodzaje towarów i usług'] == 'marchew - za 1 kg']
cebula  = df[df['Rodzaje towarów i usług'] == 'cebula - za 1 kg']
print('Dla marchwi: ')
sw_marchew = marchew.groupby(['Miesiące'])['Wartosc'].mean()
print(sw_marchew)
print('Dla cebuli: ')
sw_cebula = cebula.groupby(['Miesiące'])['Wartosc'].mean()
print(sw_cebula)

miesiace = df['Miesiące'].unique()

plt.plot(miesiace, sw_marchew, label = 'Marchew')
plt.plot(miesiace, sw_cebula, label = 'Cebula')

plt.title('Ceny produktów w poszczególnych miesiącach')
plt.xlabel('Rok 2017')
plt.ylabel('Ceny w zł za kilogram')
plt.xticks(rotation = 30)
plt.legend()
#plt.show()
plt.savefig('zad2.jpg')
