waarden = planets.groupby('method').orbital_period.aggregate(['mean', 'std'])
waarden.reset_index(inplace=True)
plt.figure(figsize=(12,8))
plt.barh(waarden.index.values, waarden['mean'], xerr=waarden['std'])
plt.yticks(waarden.index.values, waarden.method)
plt.xlabel("Orbital period")
# Met een logaritmische as kun je ze beter vergelijken.
plt.semilogx();
