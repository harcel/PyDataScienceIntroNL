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
