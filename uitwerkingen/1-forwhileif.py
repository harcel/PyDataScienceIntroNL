for i in range(10): print(i)
print()

for i in range(3,18,2): print(i)
print()

derdemacht = 1
i = 1
while derdemacht <= 1000:
    if not derdemacht %2: print(i, derdemacht)
    i += 1
    derdemacht = i**3

print()
for teken in "Python is Gaaf!":
    if teken.isupper(): print(1)
    elif teken.islower(): print(2)
    else: print(3)
      