import numpy as np   # Als je andere packages gebruikt, importeer ze hier ook. Als ze al gedefinieerd waren gebeurt er gewoon niks.
import psutil, os

print("Joepie, ik word gebruikt!")

def plus3(xx):
    """Deze functie telt 3 op bij integers, floats en alle elementen van een array.
    Als je input iets anders is, dan merk je het wel."""
    
    if type(xx) not in (float, int, np.ndarray):
        print("Daar kan ik dus mooi geen 3 bij optellen, koekie.")
        return "Jammer."
    
    resultaat = xx + 3
    
    return resultaat


def geefmeinfo():
    """Geeft een zwikkie systeeminfo. Geen argumenten, geen resultaat."""
    
    print("Het is mogelijk dat onderstaande niet op elk besturingssysteem even goed werkt...")
    print("Je werkt op een computer met {0} cpus en {1}".format(psutil.cpu_count(), psutil.virtual_memory()))
    
    return
