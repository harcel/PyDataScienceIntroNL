import numpy as np
d1 = np.array([3, 6, 9])
d2 = np.array([[1.,7],[2,8],[3,9]]) # Alles wordt float, als er minstens 1 float bestaat!
print(d1)
print(d2)
print(np.shape(d2))
print(d2.shape)      # Dit geeft hetzelfde resultaat: functie in numpy vs method op het array object!

print()
print(7*d2)

print()
getransponeerd = d2.transpose()
print(getransponeerd)
reshaped = d2.reshape(2, 3)
print(reshaped)

print()
print(d2.ravel())
print(d2.reshape(6))   # Merk de verschillen op tussen de reshape en de andere methoden!

print()
print("Totale som:", d2.sum())
print("Som kolommen:", d2.sum(axis=0))  # Dit werkt ook met andere aggeregaties, zoals gemiddelde, mediaan, etc.
print("Som rijen:", d2.sum(axis=1))
