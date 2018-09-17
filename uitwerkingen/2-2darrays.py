arr = np.random.randint(0, 10, size=(5,3))
print(arr)

arr_reshaped = arr.reshape((3,5))
print(arr_reshaped)
print()
print(arr.sum(axis=0))
print(arr_reshaped.sum(axis=1)) # Deze zijn niet hetzelfde. De arrays zijn dezelfde als je van links naar rechts van boven naar beneden leest.
print()
print(arr.transpose().sum(axis=1))  # Met transpose kan dit wel, omdat de rijen en kolommen spiegelt.
