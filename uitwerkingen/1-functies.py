def pluszeven(getal):
    # Deze functie telt zeven op bij 'getal' op.
    return getal + 7

def sommetje(begin):
    # Als het een integer is, dan oneven getallen met 3 vermenigvuldigen,
    # en even getallen met 2.
    if type(begin) == int:
        return 3*begin if begin %2 else 2*begin
    # Als het een string is met 2 vermenigvuldigen
    elif type(begin) == str:
        return 2*begin
    # En als het dat allemaal niet is, tsja...
    else: 
        print("Ik weet niet wat ik moet doen als ik geen integer of string krijg....")
        
# Voorbeelden van de werking van beide functies:
print('{0} plus zeven geeft {1}'.format(12, pluszeven(12)))
print()
for xx in [2, 5, 'Hoi!', 1.2]:
    print('{0} in het sommetje geeft {1}'.format(xx, sommetje(xx)))
    