import eigenlib as lib

lib.geefmeinfo()

# get the documentation (alt-tab werkt ook!)
print(lib.plus3.__doc__)

print()
print(lib.plus3(8.))
print(lib.plus3(np.array([2., 109.])))
print(lib.plus3('stykje tekst'))
