lijstje = np.arange(2, 21, 2)
print(lijstje)
print()
lijstje *= 3
print(lijstje)
print()
lijstje+=1
print(lijstje.sum())
print()
print(np.where(lijstje % 5 == 0))
