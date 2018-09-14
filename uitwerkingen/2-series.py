import pandas as pd

# Maak dict van de twee lijsten
gemeenten = {}
for s, i in zip(Steden, Inwoners): gemeenten[s] = i

# Maak een serie.
gem = pd.Series(gemeenten)
# Omdat de dict geen volgorde kent is deze wellicht niet gesorteerd. Doe dat.
gem.sort_values(ascending=False, inplace=True)
print(gem)
print()

# Index sorteren:
opalfabet = gem.sort_index()
print(opalfabet)
