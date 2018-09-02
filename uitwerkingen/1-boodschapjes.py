mandje = {}
for item, prijs in zip(items, prijzen):
    if not item in mandje: 
        print("Hoezee! Een nieuw item, namelijk", item)
        mandje[item] = prijs
    else: 
        mandje[item] += prijs
print(mandje)
