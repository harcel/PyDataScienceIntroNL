def pluszeven(getal):
    """Deze functie telt zeven op bij 'getal' op.
    Aanroep: result = pluszeven(getal).
    """
    return getal + 7

def sommetje(begin):
    """
    """
    if type(begin) == int:
        return 3*begin if begin %2 else 2*begin
    elif type(begin) == str:
        return 2*begin
    else: 
        print("Ik weet niet wat ik moet doen als ik geen integer of string krijg....")
        
# Voorbeelden van de werking van beide functies:
print('{0} plus zeven geeft {1}'.format(12, pluszeven(12)))
print()
for xx in [2, 5, 'Hoi!', 1.2]:
    print('{0} in het sommetje geeft {1}'.format(xx, sommetje(xx)))
    