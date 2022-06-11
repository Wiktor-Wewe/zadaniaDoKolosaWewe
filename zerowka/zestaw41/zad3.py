import matplotlib.pyplot as  plt
import numpy as np
import pandas as pd

df = pd.read_csv('cechy41.csv', sep=';')

df["Cecha1"] = df["Cecha1"].str.replace(",", ".")
df["Cecha1"] = df["Cecha1"].apply(pd.to_numeric)
df["Cecha2"] = df["Cecha2"].str.replace(",", ".")
df["Cecha2"] = df["Cecha2"].apply(pd.to_numeric)

kosz1 = np.arange(0, 201, 50)
c1 = pd.cut(df.Cecha1, kosz1)

kosz2 = np.arange(0, 201, 50)
c2 = pd.cut(df.Cecha2, kosz2)

x = np.arange(0, 544, 1)

plt.subplot(1,2,1)
plt.barh(df.Cecha1, x, color='violet', label = 'Cecha 1')
plt.xlabel('wartosci')
plt.ylabel('Dana cecha')
plt.title('Wykresy cechy 1')

plt.subplot(1,2,2)
plt.barh(df.Cecha2, x, color='blue', label = 'Cecha 2')
plt.xlabel('wartosci')
plt.ylabel('Dana cecha')

plt.title('Wykresy cechy 2')
plt.legend()
#plt.show()
plt.savefig('zad3.png')
