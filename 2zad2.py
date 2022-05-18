import matplotlib.pyplot as  plt
import numpy as np
import pandas as pd

#I punkt
data = pd.read_excel("ceny2.xlsx")

#II punkt
print(data.groupby(['Rodzaje towarów'])['Wartość'].mean()) 

#III punkt
lata = data[data['Rodzaje towarów'] == 'ryż - za 1kg']['Rok']
ryz_ceny = data[data['Rodzaje towarów'] == 'ryż - za 1kg']['Wartość']
maka_ceny = data[data['Rodzaje towarów'] == 'mąka pszenna - za 1kg']['Wartość']
plt.plot(lata, ryz_ceny, label = 'Ryż')
plt.plot(lata, maka_ceny, label = 'Mąka')
plt.title("Zmiana cen produków w poszczeólnych latach")
plt.xlabel("Lata")
plt.ylabel("Cena w zł/kg")

#punkt IV
plt.annotate('21376969', xy=(2010,2))
plt.legend()
#plt.show()
plt.savefig('zad2.jpg')
