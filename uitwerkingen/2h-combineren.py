print(population/area)
# De indices worden gebruitk om te achterhalen welke elementen bij elkaar horen.

# Strings kun je gewoon optellen!
df1 = make_df(list('AB'), range(2))
# print(df1)
df2 = make_df(list('ACB'), range(3))
# print(df2)

print(df1+df2) # Alleen overeenkomstige kolommen zijn gebruikt, en de volgorde van deze kolommen is irrelevant. Zelfde geldt voor indices.

print()
df1 = make_df('AB', [1, 2])
df2 = make_df('AB', [3, 4])
print(pd.concat([df1, df2]))   # default: ze worden onder elkaar gehangen
print()
print(pd.concat([df1, df2], axis=1))  # Nu wil concat ze naast elkaar hebben, maar indices van de rijen komen nergens overeen.
print()
df3 = make_df('AB', [1, 3])
print(pd.concat([df1, df3]))   # Er ontstaan dubbele indices. Optie "verify_integrity=True" zou dat ondervangen. Probeer maar!
print()

koffiefile = os.path.join('data', 'csvoorbeeld.csv')
koffie = pd.read_csv(koffiefile, )   # check de help voor alle opties!
koffiemerken = pd.DataFrame({'Merk':['Palazzo', "G'woon", "L'Or", "Nescafe"], "Land":['Nederland', 'Nederland', 'Frankrijk', 'Duitsland']})

# merging zonder specificatie van merge-key resulteert in een merge op overeenkomstige kolommen.
# Zonder het voorbeeld uit te werken: een outer join is altijd het grootst. Onderzoek hoe deze werkt! Hier is de outer join:
koffie.merge(koffiemerken, how='outer')
