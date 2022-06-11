import matplotlib.pyplot as  plt
import numpy as np
import pandas as pd

df = pd.read_csv('transport22.csv', sep=';')
df = df.T
df = df.rename(columns={0: "rok", 1: "jednostka", 2: "wartosc"},
               index={"motocykle ogółem": "motocykle",
                      "motocykle ogółem.1": "motocykle",
                      "motocykle ogółem.2": "motocykle",
                      "motocykle ogółem.3": "motocykle",
                      "motocykle ogółem.4": "motocykle",
                      "motocykle ogółem.5": "motocykle",
                      "motocykle ogółem.6": "motocykle",
                      "samochody osobowe": "samochody",
                      "samochody osobowe.1": "samochody",
                      "samochody osobowe.2": "samochody",
                      "samochody osobowe.3": "samochody",
                      "samochody osobowe.4": "samochody",
                      "samochody osobowe.5": "samochody",
                      "samochody osobowe.6": "samochody",
                      "autobusy ogółem": "autobusy",
                      "autobusy ogółem.1": "autobusy",
                      "autobusy ogółem.2": "autobusy",
                      "autobusy ogółem.3": "autobusy",
                      "autobusy ogółem.4": "autobusy",
                      "autobusy ogółem.5": "autobusy",
                      "autobusy ogółem.6": "autobusy"})
df.reset_index(inplace=True)
df = df.rename(columns={"index": "typ"})

df["wartosc"] = df["wartosc"].str.replace(" ", "")
df["wartosc"] = df["wartosc"].apply(pd.to_numeric)

#wybieram 2010 i 2011
moto = df[df['typ']=="motocykle"]
moto2010 = moto[moto['rok']=='2010']['wartosc']
moto2011 = moto[moto['rok']=='2011']['wartosc']

samo = df[df['typ']=="samochody"]
samo2010 = samo[samo['rok']=='2010']['wartosc']
samo2011 = samo[samo['rok']=='2011']['wartosc']

auto = df[df['typ']=="autobusy"]
auto2010 = auto[auto['rok']=='2010']['wartosc']
auto2011 = auto[auto['rok']=='2011']['wartosc']

rok2010wartosci = np.array([float(moto2010), float(samo2010), float(auto2010)])
rok2011wartosci = np.array([float(moto2011), float(samo2011), float(auto2011)])
nazwy = np.array(['motocykle', 'samochody', 'autobusy'])

fig, axs = plt.subplots(2)
axs[0].pie(rok2010wartosci, labels=nazwy)
axs[0].set_title("rok 2010")
axs[1].pie(rok2011wartosci, labels=nazwy)
axs[1].set_title("rok 2011")
plt.legend()
plt.savefig('zad3.jpg')