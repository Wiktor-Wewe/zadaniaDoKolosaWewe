import pandas as pd
import matplotlib.pyplot as plt
# wczytujesz dane i transponujesz je czyli kolumne zmieniasz w wiersz a wiersz w kolumne
df = pd.read_excel("./2020i2021/z3/handel3.xlsx").T
# po transpozycji kolumny nazywają się 0 i 1 więc zmieniasz ich nazwy na takie jakie chcesz
# po transpozycji na indexach czyli tak jakby nazwie każdego wiersza masz zduplikowane nazwy czyli 2x hipermarkety i żeby nie bawić sie w regex(bo przy duplikatach dodaje ci .1) to standaryzujesz nazwy
df = df.rename(columns={0: "Rok", 1: "Wartosc"}, index={
               "hipermarkety.1": "hipermarkety", "supermarkety.1": "supermarkety", "domy towarowe.1": "domy towarowe", "domy handlowe.1": "domy handlowe"})
# usuwasz indexy czyli wspomiane wyżej opisania wierszy
df.reset_index(inplace=True)
# zmieniasz nazwe index(domyślnie po resecie) na typ czy co tam sobie wyśnisz
df = df.rename(columns={"index": "Typ"})
# i tutaj już normalne rzeczy
wszystko1 = df[df["Rok"] == 2017]["Wartosc"].sum()
x1 = df[df["Rok"] == 2017].groupby("Typ")["Wartosc"].sum()
x1 /= wszystko1
plt.pie(x1, labels=df["Typ"].unique())
plt.show()
