def fibonacci(n, start1=1, start2=1, verbose=False):
    # Als de input kleiner is dan twee, dan kan start1 of start2 terug.    
    if n<= 2:
        print('Voor een n kleiner dan twee betekent dit vrij weinig allemaal....')
        return start1 if n == 1 else start2 if n==2 else "Uhm..."
    
    # Je hebt altijd de vorige twee getallen nodig.
    tweeterug = start1
    eenterug = start2
    
    # Eerste twee getallen vast printen voor als men dingen geprint wil zien.
    if verbose:
        print(1, start1)
        print(2, start2)
        
    # Alle andere getallen genereren.
    for i in range(3,n):
        # Het volgende getal is de som van de vorige twee
        som = eenterug + tweeterug
        # Voor de volgende iteratie zijn "het vorige getal en die daarvoor" eentje verder in de lijst
        tweeterug = eenterug
        eenterug = som
        if verbose: print(i, som)
    
    # Geef als resultaat het laatste getal in de reeks terug
    return som
