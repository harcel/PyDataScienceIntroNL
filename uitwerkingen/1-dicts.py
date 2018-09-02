# Dit kan op twee manieren. Ofwel eerst definieren en dan vullen, ofwel meteen definieren met key/value-pairs erin:
boodschappen = {}
boodschappen['aardappelen'] = 1.49
boodschappen['cola'] = 2.50
boodschappen['brood'] = 1.79
print(boodschappen)
print()
boodschapjes = {'koekjes':1.29, 'thee':0.79, 'dropjes':2.49}
print(boodschapjes)
print()
print('cola' in boodschappen, 'cola' in boodschapjes)
print('Brood kost:', boodschappen['brood'])
print()
boodschappen[2] = 3.00
boodschappen[2.34] = 'lalala'
boodschappen[True] = True
boodschappen[(1, 2, 'aap')] = "Hier is de key zelfs een tuple (lijst waarvan je de waarden niet kunt aanpassen)!"
print(boodschappen)