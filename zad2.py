import matplotlib.pyplot as  plt
import numpy as np
import pandas as pd

df = pd.read_excel('ceny1.xlsx')
print(df)

rok2014 = df[df["Rok"]==2014].Wartosc
rok2015 = df[df["Rok"]==2015].Wartosc
rok2016 = df[df["Rok"]==2016].Wartosc
miesiace = df["Miesiące"].unique()
plt.figure(figsize=(12,5))
plt.plot(miesiace, rok2014, label="Rok 2014")
plt.plot(miesiace, rok2015, label="Rok 2015")
plt.plot(miesiace, rok2016, label="Rok 2016")
plt.title("Ceny za 1kg ryżu na przełomie lat")
plt.xlabel("Miesiące")
plt.ylabel("Cena w zł")
plt.text(1, 4, '21376969')

plt.legend()
plt.savefig('zad2.png')
