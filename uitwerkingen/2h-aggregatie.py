# Voer de regels een voor een uit om de resultaten te zien.
planets.describe()
planets.groupby('method')['year'].describe()   # count is nu het aantal met de betreffende methode.
planets.groupby('year')[['mass', 'distance']].aggregate(['min', np.median])

decennium = 10 * (planets['year'] // 10)   # // is "floor division"
decennium = decennium.astype(str) + 's'    # een s erachter ziet er meer uit als decennium
decennium.name = 'decennium'               # een naam werkt goed in de tabel zometeen, zie linksboven
planets.groupby(['method', decennium])['number'].sum().unstack().fillna(0)
