x = np.array([1, 2, 3])
y = np.array([30, 20, 10])
print(np.hstack([x, y]))
print(np.hstack([x, y, y, y]))
print()
grid = np.array([[1, 2, 3],
                 [4, 5, 6]])
print(grid)
print()
print(np.vstack([grid, 10*grid]))
print()
print(np.hstack([grid, 10*grid]))

# COncatenate bestaat nog steeds voor hoger dimensionale arrays. 
# Er bestaat nog dstack voor 3D arrays, maar daar houdt het op.
# Bovendien is concatenate een algemenere oplossing:
#  - 1 functie voor concatenation langs welke as dan ook.
#  - Syntax consistent met andere numpy functionaliteit.
# 
# (h/v/d)stack worden gezien als "convenience functions".

