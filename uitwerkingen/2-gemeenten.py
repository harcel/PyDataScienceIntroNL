excelletje = os.path.join("data", "Gemeenten.xlsx")
gemeente = pd.read_excel(excelletje)
gemeente.head()

# In stapjes opgebouwd, doen we eerst de groupby, dan sommeren we de inwoners kolom en dan sorteren we de waarden:
perprov = gemeente.groupby('Provincie')   # Dit resulteert in een "groupby Object", verifieer dat. Je kunt geen data zien!
aantal_inw = perprov.Inwoners.sum()       # Nu heb je wel degelijk een nieuw dataobject. Wat voor een?
print(aantal_inw.sort_values(ascending=False))  # Sorteren met een keyword

# Op een regel zet je die bewerkignen gewoon achetr elkaar:
print(gemeente.groupby('Provincie').Inwoners.sum().sort_values(ascending=False))

# "geen" is geen missende data. Python spreekt helemaal geen Nederlands.

print("\nTotaal aantal inwoners:", aantal_inw.sum())
print()

# Totaal inkomen per gemeente:
gemeente["Totaal inkomen"] = gemeente.Gemiddeld_inkomen * gemeente.Inwoners
print("Gemiddeld inkomen per provincie:", round(gemeente.groupby('Provincie')["Totaal inkomen"].sum() / gemeente.groupby('Provincie').Inwoners.sum(), 0))
print()
# Ook proberen om dit met een functie op te lossen.
def gewogen_gem(waarden, gewichten, groep):
    return (waarden * gewichten).groupby(groep).sum() / gewichten.groupby(groep).sum()

print(gewogen_gem(gemeente.Gemiddeld_inkomen, gemeente.Inwoners, gemeente.Provincie))
print()

# Met lambda notatie, voor gevorderden (Let op al die NaNs! Wat betekent dit voor pandas aggregaties?):
gemeente.groupby('Provincie').apply(lambda x: np.average(x.Gemiddeld_inkomen, weights=x.Inwoners))
# Probeer deze laatste methode te begrijpen! Lambda functies zijn abstract, maar handige hulpmiddelen!

