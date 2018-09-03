import sys, os, time
print(sys.path)                       # Alle directories waarin Python zoekt naar je programma's
print(sys.platform)                   
print(sys.version)                    # Als het goed is vind je hier een Anaconda versie van Python, waarschijnlijk 3.6

print()
print(os.listdir())
print(os.getcwd())                    # getcwd staat voor "get current working directory"
print()
huidigedir = os.getcwd()              # Ik sla deze op in een variabele om er later makkelijk naar terug te kunnen 
os.chdir('uitwerkingen')
print(os.listdir())
os.chdir(huidigedir)
print(os.getcwd())
print()
print(os.listdir('uitwerkingen'))

print()
print(time.time())                    # Als je zin hebt kun je de eenheid die hierbij hoort opzoeken.

def slaapmaarzacht(duur):
    begin = time.time()
    print("Welterusten")
    time.sleep(duur)
    print("Mogguh!")
    return time.time() - begin

print(slaapmaarzacht(3))
