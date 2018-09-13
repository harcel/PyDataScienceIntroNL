# Hints in de opgave: beide vectoren hebben lengte 3:
#  - Het aantal rijen komt van de kolomvector, en andersom.
#  - De symmetrie leert je dat de rij en kolomvector hetzelfde moeten zijn.
#  - De waarden op de diagonaal zijn de som van de elementen met dezelfde indez in beide inputs. 
#  - Met de identieke rij- en kolomvector weet je dus dat het de waarden op de diagonaal gedeeld door twee moet zijn.

a = np.arange(3)
b = np.arange(3)[:, np.newaxis]

print(a)
print(b)

a+b

