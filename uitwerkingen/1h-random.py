import numpy as np
# Random getallen, met een uniforme verdeling tussen 0 en 1 komen uit np.random.random(). Het argument geeft het aantal.
uniform = np.random.random(1000) * 10
# De normale verdeling zit in np.random.normal(), de eerste twee argumenten zijn het gemiddelde en de standaarddeviatie.
normaal = np.random.normal(2, 3, size=1000)

print(len(uniform), np.mean(uniform), np.std(uniform), np.median(uniform), np.sum(uniform))
print(len(normaal), normaal.mean(), normaal.std(), np.median(normaal), normaal.sum())
# Merk op dat median niet als method is gedefinieerd!

def cumulatief(arr):
    return np.cumsum(arr)

# Je kunt dat ook met de hand programmeren:
def cumulatief_met_de_hand(arr):
    #definieer voor het gemak ene array van nullen
    lengte = len(arr)
    resultaat = np.zeros(lengte)
    for ii in range(lengte):
        resultaat[ii] = np.sum(arr[:ii+1])
    return resultaat

print(cumulatief(uniform)[-1] == np.sum(uniform))
print(cumulatief_met_de_hand(uniform)[-1] == np.sum(uniform))
