import matplotlib.pyplot as  plt
import numpy as np
import pandas as pd

#I punkt
df = pd.read_csv('nieruchomosci2.csv', sep=';').T

#II punkt
df = df.rename(columns={0: "metraz", 1: "rok", 2: "wartosc"},
               index={"rynek pierwotny": "pierwotny",
                      "rynek pierwotny.1": "pierwotny",
                      "rynek pierwotny.2": "pierwotny",
                      "rynek pierwotny.3": "pierwotny",
                      "rynek wtórny": "wtorny",
                      "rynek wtórny.1": "wtorny",
                      "rynek wtórny.2": "wtorny",
                      "rynek wtórny.3": "wtorny"})
df.reset_index(inplace=True)
df = df.rename(columns={"index": "typ"})
print(df)

#III i  IV punkt
df["wartosc"] = df["wartosc"].str.replace(" ", "")
df["wartosc"] = df["wartosc"].apply(pd.to_numeric)

pierwotny = df[df['typ']=='pierwotny']
nazwy_p = pierwotny.metraz
wartosci_p = pierwotny.wartosc

wtorny = df[df['typ']=='wtorny']
nazwy_w = wtorny.metraz
wartosc_w = wtorny.wartosc

fig, axs = plt.subplots(2)
axs[0].pie(wartosci_p, labels=nazwy_p)
axs[0].set_title("Rynek pierwotny")
axs[1].pie(wartosc_w, labels=nazwy_w)
axs[1].set_title("Rynek wtórny")

plt.show()
