def fibonacci(n, start1=1, start2=1, verbose=False):
    """ Een functie die het n'de getal in de fibonaccireeks print.
    Aanroep: fibonacci(n, start1=1, start2=1, verbose=False)
    Arguments:
        n: de reeks wordt tot het n'de getal bepaald. Het n'de getal wordt ook teruggegeven.
            Moet groter zijn dan 2.
    Keywords:
        start1: Het eerste getal in de reeks. Default: 1
        start2: Het tweede getal in de reeks. Default: 1
        verbose: print optioneel alle getallen in de reeks. Default: False
        
    Returns: Het n'de getal in de fibonaccireeks gedefinieerd door start1 en start2
    """
    
    if n<= 2:
        print('Voor een n kleiner dan twee betekent dit vrij weinig allemaal....')
        return start1 if n == 1 else start2 if n==2 else "Uhm..."
    
    
    tweeterug = start1
    eenterug = start2
    if verbose:
        print(1, start1)
        print(2, start2)
    for i in range(3,n):
        som = eenterug + tweeterug
        tweeterug = eenterug
        eenterug = som
        if verbose: print(i, som)
    
    return som
