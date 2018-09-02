# Aan het type van het resultaat kun je zien dat door het importeren van de numpy variant, de andere is overschreven (probeer ook nog een keer zonder de numpy import):
print(type(wortel16))

# Een oplossing om beide varianten beschikbaar te hebben is om een namespace mee te geven:
import math as m
import numpy as np

print(m.sqrt(9), type(m.sqrt(9)))
print(np.sqrt(9), type(np.sqrt(9)))
