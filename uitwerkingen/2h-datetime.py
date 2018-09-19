langereeks = pd.Series(np.random.randn(1000),
                      index=pd.date_range('1/1/2010', periods=1000))
# print(langereeks)
print()
print(langereeks['2011-08'])   # Selecteert alle indices die in die periode vallen!
print()
# Om de entries uit de laatste twee maanden te pakken, bepaal ik laatste datum, neem de maand daarvoor, en ga op de eerste van die maand zitten
laatste_maand = langereeks.index.max().year, langereeks.index.max().month -1, 1
# vanaf daar neem ik de hele series
nieuwereeks = langereeks[dt.datetime(*laatste_maand):]     # de * zorgt ervoor dat de drie waarden uit de tuple de functie ingaan, inplaats van de tuple zelf.
# De truncate functies kan dit ook:
nieuwereeks2 = langereeks.truncate(before=dt.datetime(*laatste_maand)) 
